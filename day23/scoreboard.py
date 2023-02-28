from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.setpos(-280, 280)
        self.update_screen()

    def game_over(self):
        self.setpos(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_screen()

    def update_screen(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)