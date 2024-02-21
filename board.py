from turtle import Turtle

class Borard(Turtle):
    def __init__(self):
        super(Borard, self).__init__()
        self.color('white')
        self.hideturtle()
        self.penup() #method 不會有繪製線條
        self.scoreboard = 0
        self.level= 0 
        self.ballspeed = 0
        self.update_board()
        
        #       super().__init__()
        # self.color("white")
        # self.penup()
        # self.hideturtle()
        # self.l_score = 0
        # self.r_score = 0
        # self.update_scoreboard()
    Borardycor = 250    
    
    def update_board(self):
        self.clear()
        self.goto(-250,self.Borardycor)
        self.write(f'SCORE:{self.scoreboard}', align="center", font=("Courier", 30, "normal"))
        self.goto(0, self.Borardycor)
        self.write(f'LEVEL:{self.level}', align="center", font=("Courier", 30, "normal"))
        self.goto(250, self.Borardycor)
        self.write(f'SPEED:{self.ballspeed}', align="center", font=("Courier", 30, "normal"))

    def plusscore(self):
        self.scoreboard+=1
        self.update_board()
    
    def pluslevel(self):
        self.level+=1
        self.update_board()
        
    def plusspeed(self):
        self.speed+=1
        self.update_board()