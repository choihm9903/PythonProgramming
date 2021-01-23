import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

first = True

positions = []

def mousegoto1(x,y):
    global first
    if first:
        t1.penup()
        t1.goto(x,y)
        t1.pendown()
        first = False
    else:
        t1.goto(x,y)
    positions.append(x)
    positions.append(y)

def mousegoto2(x,y):
    if len(positions) > 2:
        t1.goto(x,y)
        t1.goto(positions[0],positions[1])
        positions.append(x)
        positions.append(y)
        positions.append(positions[0])
        positions.append(positions[1])

def reset():
    t1.clear()
    for i in range(0,len(positions),2):
        t1.goto(positions[i],positions[i+1])

win.onclick(mousegoto1)
win.onclick(mousegoto2,3)
win.onkey(reset,"r")
win.onkey(reset,"R")

win.listen()
turtle.mainloop()
