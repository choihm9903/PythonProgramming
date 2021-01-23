import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

t1.penup()
t1.goto(100,100)
posturtle = t1.pos()
t1.home()
t1.pendown()

def Giyuk(length):
    t1.fd(length)
    t1.rt(90)
    t1.fd(length)

def Draw(length):
    a = 1
    while a <= 8:
        t1.penup()
        t1.setpos(posturtle)
        t1.pendown()
        Giyuk(length)
        t1.lt(45)
        a = a + 1

Draw(100)
