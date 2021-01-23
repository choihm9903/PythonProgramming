import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

position = t1.pos()

def right():
    position = t1.pos()
    t1.goto(position[0]+50,position[1])

def left():
    position = t1.pos()
    t1.goto(position[0]-50,position[1])
    
def up():
    position = t1.pos()
    t1.goto(position[0],position[1]+50)
    
def down():
    position = t1.pos()
    t1.goto(position[0],position[1]-50)

win.onkey(right,"Right")
win.onkey(left,"Left")
win.onkey(up,"Up")
win.onkey(down,"Down")

win.listen()
turtle.mainloop()
