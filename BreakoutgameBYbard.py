# import turtle
# import tkinter

# # 設定遊戲畫面
# screen = turtle.Screen()
# screen.setup(width=600, height=400)
# screen.title("Breakout")

# # 設定球拍
# paddle = turtle.Turtle()
# paddle.shape("square")
# paddle.penup()
# paddle.setposition(0, -250)

# # 設定球
# ball = turtle.Turtle()
# ball.shape("circle")
# ball.penup()
# ball.setposition(0, 0)

# # 設定磚塊
# bricks = []
# for i in range(4):
#     for j in range(10):
#         brick = turtle.Turtle()
#         brick.shape("square")
#         brick.penup()
#         brick.setposition(-250 + 50 * j, 200 - 50 * i)
#         bricks.append(brick)

# # 設定計分
# score = 0
# score_text = turtle.Turtle()
# score_text.hideturtle()
# score_text.penup()
# score_text.setposition(250, 250)

# # 遊戲循環
# while True:

#     # 處理球的運動
#     ball.setx(ball.xcor() + 5)
#     ball.sety(ball.ycor() + 5)

#     # 檢查球是否碰到邊界
#     if ball.xcor() > 300 or ball.xcor() < -300:
#         ball.setxcor(-ball.xcor())

#     if ball.ycor() > 250:
#         ball.setycor(-250)

#     # 檢查球是否碰到球拍
#     if ball.ycor() < -240 and ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50:
#         ball.setycor(-ball.ycor())

#     # 檢查球是否碰到磚塊
#     for brick in bricks:
#         if ball.xcor() > brick.xcor() - 25 and ball.xcor() < brick.xcor() + 25 and ball.ycor() > brick.ycor() - 25 and ball.ycor() < brick.ycor() + 25:
#             brick.hideturtle()
#             bricks.remove(brick)
#             score += 1
#             score_text.clear()
#             score_text.write(f"Score: {score}", align="right")

#     # 檢查遊戲是否結束
#     if len(bricks) == 0:
#         break

# # 遊戲結束
# screen.clear()
# score_text.clear()
# score_text.write("Game Over!", align="center")
# screen.update()

# # 等待使用者輸入
# turtle.done()


import turtle

class PaddleCreat:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(0, -(turtle.screensize()[1] // 2 + 20))  # Center y position

    def go_right(self):
        if self.paddle.xcor() < turtle.screensize()[0] // 2:
            new_x = self.paddle.xcor() + 20
            self.paddle.goto(new_x, self.paddle.ycor())

    def go_left(self):
        if self.paddle.xcor() > -turtle.screensize()[0] // 2:
            new_x = self.paddle.xcor() - 20
            self.paddle.goto(new_x, self.paddle.ycor())


class EXscreen(Screen):
    def __init__(self):
        self.setup(width=500, height=400)
        self.bgcolor("black")
        self.title("BreakOut")
        self.tracer(0)

        # Create a PaddleCreat instance and add it to the screen
        self.paddle = PaddleCreat()
        self.addshape("paddle", self.paddle.paddle)  # Add paddle shape for display
        self.listen()  # Listen for keyboard events

        # Optionally, attach keyboard events to paddle methods
        self.onkeypress(self.paddle.go_left, "Left")
        self.onkeypress(self.paddle.go_right, "Right")

exscreen = EXscreen()

game_is_on = True
while game_is_on:
    exscreen.update()

exscreen.exitonclick()
