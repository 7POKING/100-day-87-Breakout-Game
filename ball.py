from turtle import Turtle
from random import randint
from time import time
import brickbat

class Breakball(Turtle):
    def __init__(self):
        super(Breakball, self).__init__()
        self.color('white')
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup() #method 不會有繪製線條
        self.x_move = -1*randint(1,3)
        self.y_move = -1*randint(1,3)
        self.move_speed = 0.01
        
        # self.goto(position) # 放置位置
        # self.position = position
        
    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)
        
    def x_rebound(self):
        # self.goto(-(self.xcor() + self.x_move), -(self.ycor() + self.y_move))
        self.x_move*=-1
        # self.move_speed *= 0.9
        
    def y_rebound(self):
        self.y_move*=-1
    
    def move_rest(self):
        self.goto(0,0)
    
    # def collide(self, brick):
    #     ball_pos = self.position()
    #     brick_pos= brick.position()
    #     distance = ((ball_pos[0] - brick_pos[0])**2 + (ball_pos[1] - brick_pos[1])**2)**0.5
    #     if distance < 20:
    #         print('collision detected!')
    #         return True
    #     else:
    #         return False
    
    def checkCollisonBrick(ball,obj):
        if abs(ball.xcor() - obj.xcor()) < 50 and obj.ycor() <= ball.ycor() <= obj.ycor() + 10 :
            print("colided with the brick:", obj)
            return True
        return False
                
    # def collide_bricks(self):
    #     #  if self.collide(brick):
    #     #     brick.destoryball()
    #     if self.y_move > 0:  # 球向下移动，碰撞到砖块的上方
    #         self.y_move = -self.y_move  # 反转 y 方向速度
    #     elif self.y_move < 0:  # 球向上移动，碰撞到砖块的下方
    #         self.y_move = -self.y_move  # 反转 y 方向速度
    #     if self.x_move > 0:  # 球向右移动，碰撞到砖块的左侧
    #         self.x_move = -self.x_move  # 反转 x 方向速度
    #     elif self.x_move < 0:  # 球向左移动，碰撞到砖块的右侧
    #         self.x_move = -self.x_move  # 反转 x 方向速度
             
    def collide_bricks(self, context):
        if context == "top":
            self.setheading(360 - self.heading())
            #top half of screen
        elif 180 > self.heading() >= 0:
            self.setheading(180 - self.heading())
            #bottom half
        elif 180 <= self.heading() < 360:
            self.setheading(540 - self.heading())