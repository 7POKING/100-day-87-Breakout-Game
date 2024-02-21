# TODO:  Breakout was a hit game originally coded up by Steve Wozniak before he and Jobs started Apple.
# It's a simple game that is similar to Pong where you use a ball and paddle to break down a wall.
# A good starting point is to review the lessons on Day 22 when we built the Pong game.


# 額外提示:

# 从游戏的核心机制开始： 识别突破游戏的基本元素（球拍、球、砖块、得分等），并定义它们各自的行为和交互。
# 将项目分解成可管理的任务： 列出您需要开发的每个方面，例如创建球拍、实现球运动、砖块交互、关卡设计、用户界面等。根据复杂性和依赖性优先排序任务。
# 研究和实验： 虽然避免完全的教程，但不要犹豫寻找特定的技术概念或代码片段来帮助您解决问题。 这可能涉及查看库、文档，甚至部分教程，而不必严格遵循它们。
# 记录您的进度： 做笔记、草图和代码注释，以便保持组织并在以后理解您的决定。
# 测试和迭代： 构建可测试的小组件并逐步集成它们，不断测试和改进您的工作。
# 不要害怕寻求帮助： 如果遇到困难，可以从在线论坛、社区或经验丰富的开发人员那里寻求指导。 解释您遇到的具体挑战并展示您尝试过的内容。

# 目標:
# Vscode 產生環境  https://code.visualstudio.com/docs/python/python-tutorial
# OOP
# List Comprehension
# decorater
# inheritance
# recursive

# TODO 建立的步驟細分
# 視窗
# 球拍
#球拍移動
# 球
# 球動作軌跡
# 磚塊
# 球擊中後消除方塊
# 消除方塊後計分
# 產生重啟鍵
# 特殊效果: 關卡、音效、球擊中有特效的方塊

#導入模塊 module 或 class
import tkinter
# import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Breakball
import time
from board import Borard
from brickbat import Brickbat
from level import Level

#視窗
# screen =Screen()
# screen.setup(width=800, height=500)
# screenwidth, screenheight = screen.screensize()
screen = Screen()


# 更改視窗大小
#TODO 這裡的screen.screensize()，在while loop時會被重新更新，大小會變回預設的(400,300) ********
# screenwidth, screenheight = screen.screensize()
# print(screenwidth, screenheight)
# screenwidth= screen.screensize()[0]
# screenheight= screen.screensize()[1]

screenwidth , screenheight =800, 600
screen.setup(width=screenwidth, height=screenheight)

screen.bgcolor("black")
screen.title("BreakOut")
screen.tracer(0) #動畫消失

# r_paddle = Paddle((350, 0))
mainpaddle=Paddle((0,-(screenheight/2-30)))
ball = Breakball()
borard = Borard()
brickbatlist = []


# for i in range(int(screenwidth/brickbatlist[0].shapesize()[1])):
for i in range(10):
    x = -1*screenwidth/2+50 + (screenwidth - 200) / (10 - 1) * i  # 計算物件的 X 坐标
    print(x, screenwidth, screenheight)
    brickbatlist.append(Brickbat((x, 100), 1, 3))
    # brickbatlist.append(Brickbat((100+i*15,100), 1,1))
    # print(brickbatlist)

paddleHeight = mainpaddle.shapesize()[1]
print(f'{screen.screensize()}, mainpaddle height: {paddleHeight}')

screen.listen()
#TODO 這裡的mainpaddle.goright，如果用成mainpaddle.goright() 圖形則不會動********
screen.onkeypress(mainpaddle.go_right, "Right") 
screen.onkeypress(mainpaddle.go_left, "Left")


# def collide(ball, brick):
#     ball_pos = ball.position()
#     brick_pos= brick.position()
#     distance = ((ball_pos[0] - brick_pos[0])**2 + (ball_pos[1] - brick_pos[1])**2)**0.5
#     if distance < 20:
#         print('collision detected!')
#         return True
#     else:
#         return False

#更新動畫效果
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if abs(ball.xcor()) > (screenwidth/2-10):
        ball.x_rebound()
        # print(ball.xcor(), screenwidth, ball.ycor(), screenheight)
    if ball.ycor() > (screenheight/2-10):
        ball.y_rebound()
        # print(ball.xcor(), screenwidth, ball.ycor(), screenheight)
        
    #Detect collision with paddle
    if ball.distance(mainpaddle) < 50 and ball.ycor() < -(screenheight/2-40):
        # 球的預設半徑是 30 + paddle的半高度 20  ，球拍位置是(screenheight/2-10)減掉球的半徑30
        ball.y_rebound()
        print(ball.xcor(), screenwidth, ball.distance(mainpaddle), ball.ycor(),-(screenheight/2-40) , screenheight)

    for i in range(len(brickbatlist) - 1, -1, -1): # 倒序遍历避免索引错误
        brickbat = brickbatlist[i]
        # if ball.distance(brickbat) < 10 and ball.distance(brickbat) < brickbat.ycor():
        #     brickbat.hideturtle() # 刪掉方塊
        #     ball.collide_bricks()
        #     brickbatlist.remove(brickbat) # 移除list中的物件
        #     borard.plusscore()
        if abs(ball.xcor() - brickbat.xcor()) < 50 and brickbat.ycor() <= ball.ycor() <= brickbat.ycor() + 10 :
            print("colided with the brick:", brickbat)
            brickbat.hideturtle() # 刪掉方塊
            # ball.collide_bricks()
            brickbatlist.remove(brickbat) # 移除list中的物件
            borard.plusscore()
        if ball.ycor() > 240:
            print("colided with the brick:")
            ball.collide_bricks("TOP")
        if brickbatlist == []:
            game_is_on = False
            borard.pluslevel()
                
        
    if ball.ycor() < -screenheight/2:
        ball.move_rest()
        
    ball.move()

    
    
    
    
    
    
    
    

#Screen在按下後才離開的method
screen.exitonclick()




#其他###############################################################
# TODO 為什麼用成
# screen.onkeypress(mainpaddle.go_right(), "Right") 
# screen.onkeypress(mainpaddle.go_left(), "Left")
# 會不能用Right 或 Left 移動?
#答案 因為是參數，被調用的參數而不適使用method執行後的結果為參數
# 在你提供的程式碼中，screen.onkeypress() 方法的第一個參數應該是函數的引用，而不是函數的調用。這意味著你應該傳遞函數的名稱，
# 而不是在函數名後面加上括號和參數。當你使用括號調用函數時，它會立即執行該函數，並將返回值（如果有的話）傳遞給 screen.onkeypress() 方法，
# 而不是等到按鍵被按下時才執行。
# 因此，正確的做法是將函數名稱作為參數傳遞給 screen.onkeypress() 方法


# screen.onkey(r_paddle.go_up, "Right")
# screen.onkey(r_paddle.go_down, "Left")
# screen.onkey(l_paddle.go_up, "w")
# screen.onkey(l_paddle.go_down, "s")


# # paddle = Paddle(screenheight=screenheight)
# paddle = Turtle()
# paddle.color("white")
# paddle.shape("square")
# paddle.shapesize(stretch_wid=1, stretch_len=5)
# paddle.penup() #method 不會有繪製線條 
# paddle.goto(0,-(screenheight/2+20)) # 放置位置

# def go_right(): 
#     # if self.xcor() < 100/2:
#     new_x = paddle.xcor() + 20
#     print(new_x, paddle.ycor())       
#     paddle.goto(new_x, paddle.ycor())
        
# def go_left():
#     # if self.xcor() > -100/2:
#     new_x = paddle.xcor() -20
#     print(new_x, paddle.ycor())
#     paddle.goto(new_x, paddle.ycor())

# screen.listen() #class 中的method監控指令
# # screen.onkeypress(paddle.go_left(), "Left") # 使用左箭頭鍵移動額外球拍向左
# # screen.onkeypress(paddle.go_right(), "Right") 
# screen.onkey(go_right(), "Right")
# screen.onkey(go_left(), "Left")


#按一下移動一下的方法
# screen.onkey(go_left,"Left" )
# screen.onkey(go_right,"Right" )


# 嘗試產生類別物件
# class PaddleCreat():
#     def __init__(self, *args, **kwargs):
#         self.paddle = Turtle() # class 產生物件賦值給paddle名稱
#         self.paddle.color("white")
#         self.paddle.shape("square")
#         self.paddle.shapesize(stretch_wid=1, stretch_len=5)
#         self.paddle.penup() #method 不會有繪製線條 
#         self.paddle.goto(0,-(screenheight/2+20)) # 放置位置
        
#     def go_right():
#         if paddle.xcor() < screenwidth/2:
#             new_x = paddle.xcor() + 20
#             print(new_x, paddle.ycor())       
#             paddle.goto(new_x, paddle.ycor())

#     def go_left():
#         if paddle.xcor() > -screenwidth/2:
#             new_x = paddle.xcor() -20
#             print(new_x, paddle.ycor())  
#             paddle.goto(new_x, paddle.ycor())
            
            
# class EXscreen(PaddleCreat, Screen):
#     def __init__(self):
#         self =Screen()
#         self.setup(width= 500, height= 400)
#         self.bgcolor("black")
#         self.title("BreakOut")
#         self.tracer(0) #動畫消失
#         screenwidth, screenheight = screen.screensize()
#         print(screenwidth, screenheight)
    
# exscreen =  EXscreen()



# expaddle = PaddleCreat()
# exscreen.onkeypress(expaddle.go_left,"Left" )
# exscreen.onkeypress(expaddle.go_right,"Right" )

# game_is_on = True

# expaddle.go_left()
# expaddle.go_right()

# while game_is_on:
#     screen.update()


# exscreen.exitonclick()