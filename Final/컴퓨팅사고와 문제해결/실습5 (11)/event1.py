# 1단계
import turtle

penDownState = False

win = turtle.Screen()
t1 = turtle.Turtle()
t1.shape("turtle")

# 3단계
def mousegoto(x, y):
    t1.goto(x, y)

def pd1(x, y):
    t1.pendown()
    
def pu1(x, y):
    t1.penup()
#    penDownState = not penDownState
#    if penDownState:
#        t1.pendown()
#    else:
#        t1.penup()

def keyf():
    p = t1.pos()
    t1.goto(p[0] + 10, p[1])
    #t1.fd(50)

def keyb():
    t1.back(50)

def keyrl():
    t1.left(10)
    
def home():
    t1.home()

def prpos():
    p = t1.pos()
    #print(p)
    t1.write(p)
    
t1.penup()

#mousegoto(100, 50)
# 4단계
win.onclick(mousegoto)
win.onclick(pu1, 2)
win.onclick(pd1, 3)

win.onkey(keyf, "Right")
win.onkey(keyb, "Left")
win.onkey(keyrl, "Up")
win.onkey(t1.home, 'h')
win.onkey(t1.home, 'H')
win.onkey(prpos, 'p')
win.onkey(prpos, 'P')
win.onkey(t1.penup, 'u')
win.onkey(t1.pendown, 'd')

# 5단계
win.listen()

# 6단계
turtle.mainloop()
