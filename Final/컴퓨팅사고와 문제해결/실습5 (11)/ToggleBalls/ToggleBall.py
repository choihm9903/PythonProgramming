import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

index = True

def registerImages():
    win.addshape("baseball.gif")
    win.addshape("basketball.gif")
    
def keyP():
    global index
    index = not index
    if index:
        t1.shape("baseball.gif")
    else:
        t1.shape("basketball.gif")

def g(x, y):
    global index
    index = not index
    if index:
        t1.shape("baseball.gif")
    else:
        t1.shape("basketball.gif")

registerImages()
t1.shape("baseball.gif")
win.onkey(keyP, 'p')
win.onclick(g)

win.listen()
turtle.mainloop()

