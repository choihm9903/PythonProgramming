import turtle
win = turtle.Screen()
t1 = turtle.Turtle()


for i in range(6):
    win.addshape("dice"+str(i+1)+".gif")

import random

def dice():
    n = random.randint(1,6)
    if n == 1:
        t1.shape("dice1.gif")
    elif n == 2:
        t1.shape("dice2.gif")
    elif n == 3:
        t1.shape("dice3.gif")
    elif n == 4:
        t1.shape("dice4.gif")
    elif n == 5:
        t1.shape("dice5.gif")
    else:
        t1.shape("dice6.gif")
    t1.stamp()
    t1.shape("classic")

win.onkey(dice,"r")
win.onkey(dice,"R")
win.onkey(turtle.bye,"q")
win.onkey(turtle.bye,"Q")

win.listen()
turtle.mainloop()


    
