from turtle import Turtle
import random

colors = ["red", "orange", "blue", "yellow", "black"]



class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            cars = Turtle()
            cars.shape("square")
            cars.shapesize(stretch_wid=1, stretch_len=2)
            cars.penup()
            cars.color(random.choice(colors))
            random_y = random.randint(-250, 250)
            cars.goto(300, random_y)
            self.all_cars.append(cars)

    def move_car(self):
        for i in self.all_cars:
            i.bk(self.car_speed)

    def speed_up(self):
        self.car_speed += 5
