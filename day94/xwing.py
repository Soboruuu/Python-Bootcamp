import turtle
import time
import missile

screen = turtle.Screen()
# Add x-wing image on screen.
screen.register_shape('assets/x-wing.gif')

class Xwing(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        # set player(turtle) as x-wing
        self.shape('assets/x-wing.gif')
        self.color('white')
        self.penup()
        self.setpos(position)
        self.fire_delay = 0.5  # Set the delay between firing of missiles
        self.last_fired_time = 0  # Initialize the time of the last missile firing to 0

    def go_left(self):
        if self.xcor() > -380:
            new_x = self.xcor() - 10
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 370:
            new_x = self.xcor() + 10
            self.goto(new_x, self.ycor())

    def fire(self):
        # Check if enough time has passed since the last missile was fired
        current_time = time.time()
        if current_time - self.last_fired_time < self.fire_delay:
            return missile.NoMissile((500,500))
            # Fire a missile
        mis = missile.Missile(self.pos())
        mis.move()
        self.last_fired_time = current_time
        return mis
