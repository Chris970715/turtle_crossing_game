from turtle import Turtle
import random
import time

time_list = [0.1, 0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):

        self.all_cars = []
        self.carSpeed = STARTING_MOVE_DISTANCE


    def setup(self):
        t = random.randint(1,6)
        if t == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len = 2, stretch_wid = 1)
            new_car.color(random.choice(COLORS))

            self.x_position = 310
            self.y_position = random.randint(-280, 300)

            new_car.goto(self.x_position, self.y_position)

            self.all_cars.append(new_car)


    def move(self):

        for car in self.all_cars:
            car.backward(self.carSpeed)


    def level_up(self):
        self.carSpeed += MOVE_INCREMENT
