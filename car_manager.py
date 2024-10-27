import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.penup()
        self.goto(0, 400)
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate(self):
        variable = random.randint(1, 6)
        if variable == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.turtlesize(1, 2)
            new_car.penup()
            new_car.goto(310, random.choice(range(-250, 250)))
            self.cars.append(new_car)

    def move(self):
        for each in self.cars:
            each.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT