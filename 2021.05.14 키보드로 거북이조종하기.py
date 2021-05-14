import turtle
t = turtle.Turtle()

t.width(3)
t.shape("circle")
t.shapesize(3,3) #크기

#무한반복
while True:
    command = input("명령어 입력:")
    if command == "l":
        t.left(90)
        t.forward(100)
    if command == "r":
        t.right(90)
        t.forward(100)
