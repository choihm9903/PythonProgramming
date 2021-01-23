import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def Giyuk(length):
    t1.fd(length)
    t1.rt(90)
    t1.fd(length)

def Draw(length):
    for angle in range(45,361,45):
        Giyuk(length)
        t1.penup()
        t1.home()
        t1.pendown()
        t1.setheading(angle)

Draw(100)
