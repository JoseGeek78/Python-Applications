from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.X_move = 10
        self.Y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        new_X = self.xcor() + self.X_move
        new_Y = self.xcor() + self.Y.move
        self.goto(new_X, new_Y)
        
    