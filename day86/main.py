from turtle import *
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard, Life
from brick import Brick
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

scoreboard = Scoreboard()
life = Life()

# Bricks. Total 6 rows 9 columns. x= from -320 to 320 by 80, y= from 0 to 200 by 40.
bricks = []
y = 0
colors=['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for i in range(6):
    color = colors[i]
    positions = [(x, y) for x in range(-320, 321, 80)]
    y += 40
    for position in positions:
        brick = Brick(position, color)
        bricks.append(brick)

paddle = Paddle((0, -280))
ball = Ball()


screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_started = False

def start_game():
    global game_started
    game_started = True

screen.onkey(start_game, "space")


while life.life > 0 and len(bricks) > 0:
    screen.listen()
    if game_started:
        time.sleep(ball.move_speed)
        ball.move()

    # detect ball's collision with top of the screen or with the paddle -> bounce
    if ball.ycor() > 280 or (ball.ycor() < -260 and
            ball.xcor() > paddle.xcor() - 50 and
            ball.xcor() < paddle.xcor() + 50):
        ball.bounce_y()

    # detect ball's collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 40 and ball.collide_rect(brick):
            bricks.remove(brick)
            brick.hideturtle()  # hide the brick from the screen
            scoreboard.point()  # increase the player's score
            ball.bounce_y()

    # detect ball's collision with side walls -> bounce
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # detect ball going off the bottom of the screen -> reset ball and subtract a life
    if ball.ycor() < -280:
        life.decrease_life()
        ball.reset_ball()

    screen.update()

if life.life == 0 or len(bricks) == 0:
    life.gameover()
    screen.update()

screen.exitonclick()
