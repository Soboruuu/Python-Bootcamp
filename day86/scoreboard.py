from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(300, 230)
        self.write(f'Point: {self.score}', align="center", font=("Arial", 30, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()

class Life(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.life = 3
        self.update_life()

    def update_life(self):
        self.clear()
        self.goto(-300, 230)
        self.write(f'Life: {self.life}', align="center", font=("Arial", 30, "normal"))

    def decrease_life(self):
        self.life -= 1
        self.update_life()

    def gameover(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, -180)
        self.write('GAME OVER', align="center", font=("Arial", 50, "normal"))

