from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super.__init__()
        self.shape('cirlce')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed('fastest')
        randomX = random.randint(a=-280, b=280)
        randomY = random.randint(a=-280, b=280)
        self.goto(randomX, randomY)
