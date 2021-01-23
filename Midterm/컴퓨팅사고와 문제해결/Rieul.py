import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

# 'ㄹ'자 그리는 코드
def moveTo(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()
    
def drawRieul(x, y, sizex, sizey):
    moveTo(x, y)
    t1.setheading(0)
    t1.fd(sizex)
    t1.rt(90)
    t1.fd(sizey / 2)
    t1.rt(90)
    t1.fd(sizex)
    t1.lt(90)
    t1.fd(sizey / 2)
    t1.lt(90)
    t1.fd(sizex)

drawRieul(-350, -50, 130, 120)
drawRieul(-50, 200, 130, 120)
drawRieul(250, 200, 130, 120)