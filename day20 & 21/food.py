import random
from turtle import Turtle
class Food(Turtle):
    def __int__(self):
        super().__init__() # initialize the super class Turtle
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)