import turtle

class NoMissile(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()
        self.setpos(position)

class Missile(turtle.Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.shape('square')
        self.shapesize(stretch_wid=0.1, stretch_len=1)
        self.size = 1
        self.color('lightgreen')
        self.penup()
        self.setpos(position)

    def move(self):
        self.forward(10)
        if self.ycor() > 300:
            self.hideturtle()
            self.clear()
        else:
            turtle.ontimer(self.move, 10)

    def collide_rect(self, other):
        self_left = self.xcor() - self.size / 2
        self_right = self.xcor() + self.size / 2
        self_top = self.ycor() + self.size / 2
        self_bottom = self.ycor() - self.size / 2

        other_left = other.xcor() - other.width / 2
        other_right = other.xcor() + other.width / 2
        other_top = other.ycor() + other.height / 2
        other_bottom = other.ycor() - other.height / 2

        if (self_right >= other_left and self_left <= other_right and
                self_bottom <= other_top and self_top >= other_bottom):
            return True
        else:
            return False

