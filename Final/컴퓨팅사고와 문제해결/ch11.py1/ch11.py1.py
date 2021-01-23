import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()

win.setup(700, 600)

win.addshape("scissors.gif")
win.addshape("rock.gif")
win.addshape("paper.gif")

t1.penup()
t1.goto(-180, 0)
t1.pendown()
t2.penup()
t2.goto(180, 0)
t2.pendown()

import random
n = random.randint(1,3)

if n == 1:
    t2.shape("scissors.gif")
elif n == 2:
    t2.shape("rock.gif")
elif n == 3:
    t2.shape("paper.gif")

def scissors():
    t1.shape("scissors.gif")
def rock():
    t1.shape("rock.gif")
def paper():
    t1.shape("paper.gif")

win.onkey(scissors,"s")
win.onkey(scissors,"S")
win.onkey(rock,"r")
win.onkey(rock,"R")
win.onkey(paper,"p")
win.onkey(paper,"P")

win.listen()
turtle.mainloop()

