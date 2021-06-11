import turtle
#색상 리스트
colors=["red","purple","blue","green","orange","pink"]
t= turtle.Turtle()
turtle.bgcolor("black")

t.speed(0)
t.width(3)
length=10

while length<500:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length+=5
