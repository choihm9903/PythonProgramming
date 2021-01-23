import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

win.addshape("baseball.gif")
win.addshape("basketball.gif")
win.addshape("football.gif")
win.addshape("tennisball.gif")
win.addshape("volleyball.gif")

def ball(num):
    if num == 0:
        t1.shape("baseball.gif")
    elif num == 1:
        t1.shape("basketball.gif")
    elif num == 2:
        t1.shape("football.gif")
    elif num == 3:
        t1.shape("tennisball.gif")
    elif num == 4:
        t1.shape("volleyball.gif")

def reset():
    ball(0)

def up():
    global index
    if index == 0:
        ball(0)
        index += 1
    elif index == 1:
        ball(1)
        index += 1
    elif index == 2:
        ball(2)
        index += 1
    elif index == 3:
        ball(3)
        index += 1
    else:
        ball(4)
        index = 0
    return index

def down(x,y):
    global index
    if index == 4:
        ball(4)
        index -= 1
    elif index == 3:
        ball(3)
        index -= 1
    elif index == 2:
        ball(2)
        index -= 1
    elif index == 1:
        ball(1)
        index -= 1
    else:
        ball(0)
        index = 4
    return index
        
ball(0)
index = 0
win.onkey(turtle.bye,"q")
win.onkey(turtle.bye,"Q")
win.onkey(reset,"b")
win.onkey(reset,"B")
win.onkey(up,"n")
win.onkey(up,"N")
win.onclick(down,1)

win.listen()
turtle.mainloop()
