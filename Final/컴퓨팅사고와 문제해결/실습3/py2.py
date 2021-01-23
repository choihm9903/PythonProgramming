import turtle
win = turtle.Screen()
tp = turtle.Turtle()
tc = turtle.Turtle()
import random

win.setup(700,600)
win.addshape("scissors.gif")
win.addshape("rock.gif")
win.addshape("paper.gif")

tp.penup()
tp.goto(-180,0)
tp.pendown()

tc.penup()
tc.goto(180,0)
tc.pendown()

def result(p,c):
    if p == 1:
        if c == 1:
            print("비겼습니다.")
        elif c == 2:
            print("컴퓨터가 이겼습니다.")
        else:
            print("사람이 이겼습니다.")
    elif p == 2:
        if c == 1:
            print("사람이 이겼습니다.")
        elif c == 2:
            print("비겼습니다.")
        else:
            print("컴퓨터가 이겼습니다.")
    else:
        if c == 1:
            print("컴퓨터가 이겼습니다.")
        elif c == 2:
            print("사람이 이겼습니다.")
        else:
            print("비겼습니다.")

def player(p):
    if p == 1:
        tp.shape("scissors.gif")
    elif p == 2:
        tp.shape("rock.gif")
    else:
        tp.shape("paper.gif")

def computer(c):
    if c == 1:
        tc.shape("scissors.gif")
    elif c == 2:
        tc.shape("rock.gif")
    else:
        tc.shape("paper.gif")

def scissors():
    c = random.randint(1,3)
    player(1)
    computer(c)
    result(1,c)

def rock():
    c = random.randint(1,3)
    player(2)
    computer(c)
    result(2,c)

def paper():
    c = random.randint(1,3)
    player(3)
    computer(c)
    result(3,c)
    
win.onkey(scissors,"s")
win.onkey(scissors,"S")
win.onkey(rock,"r")
win.onkey(rock,"R")
win.onkey(paper,"p")
win.onkey(paper,"P")

win.listen()
turtle.mainloop()
