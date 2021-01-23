import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
win.bgpic("maze.gif")
win.setup(425,425)

position = t1.pos()
t1.penup()
t1.goto(-70,-200)
t1.pendown()

def right():
    position = t1.pos()
    t1.goto(position[0]+10,position[1])

def left():
    position = t1.pos()
    t1.goto(position[0]-10,position[1])
    
def up():
    position = t1.pos()
    t1.goto(position[0],position[1]+10)
    
def down():
    position = t1.pos()
    t1.goto(position[0],position[1]-10)

def end():
    t1.penup()
    t1.goto(0,0)
    t1.write("End")
    
win.onkey(right,"Right")
win.onkey(left,"Left")
win.onkey(up,"Up")
win.onkey(down,"Down")
win.onkey(end,"e")
win.onkey(end,"E")

win.listen()
turtle.mainloop()
