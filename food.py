from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # Turtle shape is default 20px so we stretched it to half which means 10px
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("pink")
        # Turtle animation speed
        self.speed("fastest")
        self.goRandomLocation()

    def goRandomLocation(self):
        # Our screen size is 600px x 600px
        # So we give random x and y coordinates between -300 and 300
        # Also set 20px screen offset
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
