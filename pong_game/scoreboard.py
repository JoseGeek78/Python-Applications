from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score, align="center", font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score, align="center", font=("Courier",80,"normal"))
        
    def l_point(self):
        self.l_score += 1
        