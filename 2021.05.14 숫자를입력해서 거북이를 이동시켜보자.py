import turtle
t = turtle.Turtle()
t.shape("turtle")

t.penup()
t.goto(100,100) # 거북이가 양의 값을 가지면 오는 자리
t.write
t.goto(100,0)   #거북이가 0을 가지면 오는 자리
t.write
t.goto(100,-100)#거북이가 음의 값을 가지면 오는자리
t.write

t.goto(0,0)     #거북이가 원위치로 오는 명령
t.pendown()

while True:     #반복실행
    s = turtle.textinput("","숫자를 입력하시오")
    n = int(s)

    if(n>0):
        t.goto(100,100)
    if(n==0):
        t.goto(100,0)
    if(n<0):
        t.goto(100,-100)
