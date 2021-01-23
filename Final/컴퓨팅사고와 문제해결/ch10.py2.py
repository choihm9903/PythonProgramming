import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

t1.shape("turtle")

def go():
    t1.fd(100)

win.onkey(go,"Right")
win.listen()
turtle.mainloop()
