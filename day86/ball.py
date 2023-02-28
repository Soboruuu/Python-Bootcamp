from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0,-240)
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.size = 20
        self.has_bounced_y = False
        self.has_bounced_x = False

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        self.has_bounced_y = False
        self.has_bounced_x = False

    def bounce_y(self):
        if not self.has_bounced_y:
            self.y_move *= -1
            self.has_bounced_y = True

    def bounce_x(self):
        if not self.has_bounced_x:
            self.x_move *= -1
            self.move_speed *= 0.9
            self.has_bounced_x = True

    def reset_ball(self):
        self.setpos(0,-200)
        self.move_speed = 0.1
        self.y_move *= -1
        self.has_bounced_y = False
        self.has_bounced_x = False

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
