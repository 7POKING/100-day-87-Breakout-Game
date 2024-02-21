from turtle import Turtle
from level import Level
import random

class Brickbat(Turtle):
    list = ["green", "yellow", "blue", "purple", "orange", "gray"]
    def __init__(self, position, brickbatwid, brickbatlen):
        super(Brickbat, self).__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=brickbatwid, stretch_len=brickbatlen)
        self.penup() #method 不會有繪製線條 
        self.goto(position) # 放置位置
        self.color(Brickbat.list[random.randint(0,len(Brickbat.list)-1)])
        self.position = position
   
    # def destoryBrickbat(self):
        # self.hideturtle()
    
    def brickLevelsize(self):
        Level().defaultlevel
        