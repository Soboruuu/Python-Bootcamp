from turtle import Turtle
import random


class Brick(Turtle):
    def __init__(self, position, colors):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.color(colors)
        self.penup()
        self.setpos(position)
        self.width = self.shapesize()[1] * 20
        self.height = self.shapesize()[0] * 20
