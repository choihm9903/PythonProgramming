import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def Giyuk(length):
    t1.fd(length)
    t1.rt(90)
    t1.fd(length)

def Draw(length):
    angle = 45
    while angle <= 360:
        Giyuk(length)
        t1.penup()
        t1.home()
        t1.pendown()
        t1.lt(angle)
        angle = angle + 45

Draw(100)
