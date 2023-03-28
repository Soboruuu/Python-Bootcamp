import turtle
import random
import missile

screen = turtle.Screen()
# Add imperial image on screen.
screen.register_shape('assets/invaders.gif')

class Invaders(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('assets/invaders.gif')
        self.penup()
        self.setpos(position)
        self.width = self.shapesize()[1] * 20
        self.height = self.shapesize()[0] * 20
        self.missiles = []
        self.direction = 1  # 1 for right, -1 for left
        self.move_distance = 10  # the distance to move to the right/left
        self.drop_distance = 50  # the distance to drop down when reaching the edge

    # def explode(self):
    #     self.hideturtle()
    #     screen.register_shape('assets/explode.gif')
    #     self.shape('assets/explode.gif')
    #     turtle.ontimer(lambda: self.hideturtle(), 500)

    def fire_missile(self):
        x, y = self.position()
        y -= self.height/2
        mis = missile.Missile((x, y))
        self.missiles.append(mis)
        turtle.ontimer(self.fire_missile, random.randint(1000, 3000))

    def invade(self):
        # Move the invaders to the right or left
        new_x = self.xcor() + self.direction * self.move_distance
        self.setx(new_x)

        # Check if the invaders have reached the edge of the screen
        if new_x > 360 or new_x < -360:
            # Change the direction of the invaders
            self.direction *= -1

            # Move the invaders down
            new_y = self.ycor() - self.drop_distance
            self.sety(new_y)

            # Check if any invader has reached the bottom of the screen
            if new_y < -250:
                turtle.write("Game over!", align="center", font=("Arial", 24, "normal"))
                return




