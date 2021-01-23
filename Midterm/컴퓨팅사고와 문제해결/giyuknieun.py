import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

# ㄴ
def drawNieun(size):
    t1.setheading(0)
    t1.rt(90)
    t1.fd(size)
    t1.lt(90)
    t1.fd(size)

# ㄱ
def drawGiyuk(s, t):
    t1.setheading(0)
    t1.fd(s)
    t1.rt(90)
    t1.fd(t)
    
drawGiyuk(250, 150)
drawNieun(100, 100)
