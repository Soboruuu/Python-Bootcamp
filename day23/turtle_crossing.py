from turtle import Screen, Turtle
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.screensize(600,600)
screen.tracer(0)

player = Player()
car_manager = CarManager() 
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect successfull crossing

    if player.ycor() == 290:
        player.starting_position() 
        scoreboard.level_up()
        car_manager.harder()
        


screen.exitonclick()