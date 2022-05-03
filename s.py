import turtle, random

screen = turtle.screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1 = turtle.Turtle()
t1.shape(image1)
t1.penup()
t1.goto(-300, 0)



t1.pendown()
t2.pendown()
t1.speed(1)
t2.speed(1)

for i in range (30):
    d1 = random.randint(1,50)
    t1.forward(d1)
    d2 = random.randint(1,50)
    t2.forward(d2)
