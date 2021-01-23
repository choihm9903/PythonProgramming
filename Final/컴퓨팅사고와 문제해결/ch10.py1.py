import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

t1.shape("turtle")

def go(x,y):
    t1.goto(x,y)

def position():
    position = t1.pos()
    print("x =",position[0])
    print("y =",position[1])

win.onclick(go)
win.onkey(position,"p")
win.onkey(position,"P")

win.listen()
turtle.mainloop()
