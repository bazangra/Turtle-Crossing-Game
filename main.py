import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate()
    car_manager.move()
    if player.ycor() == 280:
        player.refresh()
        scoreboard.level_up()
        car_manager.speed_up()
    for each in car_manager.cars:
        if each.distance(player) < 20:
            scoreboard.end_game()
            game_is_on = False

screen.exitonclick()
