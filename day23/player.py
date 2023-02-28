from turtle import Turtle

MOVE_DISTANCE = 10
STARTING_POSITION = (0,-280)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.starting_position()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def starting_position(self):
        self.setpos(STARTING_POSITION)
        


