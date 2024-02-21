from turtle import Turtle

# from turtle import Turtle

class Paddle(Turtle):
    
# 球拍    
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup() #method 不會有繪製線條 
        self.goto(position) # 放置位置
        self.position = position
        
        
          
    # TODO: 額外功能: 多產生一個球拍
    #產生額外的球拍，特殊功能啟動時
    # expaddle = Turtle() # class 產生物件賦值給paddle名稱
    # expaddle.color("white")
    # expaddle.shape("square")
    # expaddle.shapesize(stretch_wid=1, stretch_len=5)
    # expaddle.penup() #method 不會有繪製線條 
    # expaddle.goto(0,-(screenheight/2-10)) # 放置位置

     #球拍移動
    def go_right(self):
        print(self.position)
        if self.xcor() < -self.position[1]+70:
            new_x = self.xcor() + 20
            # print(new_x, self.ycor())       
            self.goto(new_x, self.ycor())
        
        #特殊功能: 反向球拍移動
        # try: 
        #     if expaddle.xcor() > -screenwidth/2:
        #         new_x = expaddle.xcor() -20
        #         print(new_x, expaddle.ycor())  
        #         expaddle.goto(new_x, expaddle.ycor())
            
        # except Exception:
        #     print("no expaddle")
            
    def go_left(self):
        # print(self.position[1]/2)
        if self.xcor() > self.position[1]-75:
            new_x = self.xcor() -20
            # print(new_x, self.ycor())
            self.goto(new_x, self.ycor())
        #特殊功能: 反向球拍移動
        # try:  
        #     if expaddle.xcor() < screenwidth/2:
        #         new_x = expaddle.xcor() + 20
        #         # print(new_x, expaddle.ycor())       
        #         expaddle.goto(new_x, expaddle.ycor())
        # except Exception:
        #     pass
        
        
        
        
    