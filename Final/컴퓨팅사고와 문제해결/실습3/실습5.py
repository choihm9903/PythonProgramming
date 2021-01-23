import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

win.addshape("baseball.gif")
win.addshape("basketball.gif")
win.addshape("football.gif")
win.addshape("tennisball.gif")
win.addshape("volleyball.gif")

def reset():
    t1.shape("baseball.gif")

def up():
    global n
    if n == 0:
        n += 1
        t1.shape("basketball.gif")
    elif n == 1:
        n += 1
        t1.shape("football.gif")
    elif n == 2:
        n += 1
        t1.shape("tennisball.gif")
    elif n == 3:
        n += 1
        t1.shape("volleyball.gif")
    else:
        n = 0
        t1.shape("baseball.gif")
    return n

def down(x,y):
    global n
    if n == 0:
        n = 4
        t1.shape("volleyball.gif")
    elif n == 1:
        n -= 1
        t1.shape("baseball.gif")
    elif n == 2:
        n -= 1
        t1.shape("basketball.gif")
    elif n == 3:
        n -= 1
        t1.shape("football.gif")
    else:
        n -= 1
        t1.shape("tennisball.gif")
    return n

t1.shape("baseball.gif")
n = 0
win.onkey(up,"n")
win.onkey(up,"N")
win.onclick(down,3)
win.onkey(reset,"b")
win.onkey(reset,"B")    
win.onkey(turtle.bye,"q")
win.onkey(turtle.bye,r"Q")

win.listen()
turtle.mainloop()
