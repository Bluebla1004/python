import turtle #터틀 그래픽 모듈 불러오
import random #난수모듈 불러오기

screen = turtle.Screen()
image1="front.gif"
image2="back.gif"

screen.addshape(image1)
screen.addshape(image2)

t=turtle.Turtle()
coin = random.randint(0,1)
if coin == 0:
    t.shape(image1)
    t.stamp()
else:
    t.shape(image2)
    t.stamp()
