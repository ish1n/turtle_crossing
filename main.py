from turtle import Screen
import time
from turtlemove import Start
from cars import Cars
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Start()
cars= Cars()
score=Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "w")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_car()
    for car in cars.all_cars:
        if car.distance(player)<20:
            game_on=False
            score.game_over()

    if player.ycor() >280:
        player.starting_line()
        cars.speed_up()
        score.update_level()




screen.exitonclick()
