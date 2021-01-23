import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

# ㄱ
t1.setheading(0)
t1.fd(100)
t1.rt(90)
t1.fd(100)

t1.penup()
t1.home()
t1.pendown()

# ㄴ
t1.setheading(0)
t1.rt(90)
t1.fd(100)
t1.lt(90)
t1.fd(100)
size = 100

def drawDigeud():
    t1.penup()
    t1.home()
    t1.pendown()
    t1.setheading(0)
    t1.backward(size)
    t1.right(90)
    t1.forward(size)
    t1.left(90)
    t1.forward(size)

    
drawDigeud()