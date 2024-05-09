from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


paddle = Turtle()
screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

#Calling of all classes
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()