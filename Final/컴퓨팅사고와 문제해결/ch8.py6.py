import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

t1.penup()
t1.goto(100,100)
turtlepos = t1.pos()
t1.home()
t1.pendown()


def Giyuk(length):
    t1.fd(length)
    t1.rt(90)
    t1.fd(length)

def Draw(length):
    for a in range(8):
        t1.penup()
        t1.setpos(turtlepos)
        t1.pendown()
        Giyuk(length)
        t1.lt(45)

Draw(100)
