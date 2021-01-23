import random
import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

win.addshape("rock.gif")
win.addshape("scissors.gif")
win.addshape("paper.gif")

"""
def writeResult(value, human):
    if human == "사람1":
        t = t1
    elif human == "사람2":
        t = t2
        
    if value == 0:
        t.shape("scissors.gif")
    elif value == 1:
        t.shape("rock.gif")
    else:
        t.shape("paper.gif")
"""         

def writeResult(value, t):
    if value == 0:
        t.shape("scissors.gif")
    elif value == 1:
        t.shape("rock.gif")
    else:
        t.shape("paper.gif")

human1 = random.randint(0, 2)
human2 = random.randint(0, 2)

t1.penup()
t1.goto(-200, 0)
t1.pendown()
#writeResult(human1, "사람1")
writeResult(human1, t1)

t2.penup()
t2.goto(200, 0)
t2.pendown()

#writeResult(human2, "사람2")
writeResult(human2, t2)

t3.penup()
t3.goto(-40, -200)
if human1 == 0:
    if human2 == 0:
        t3.write("무승부")
    elif human2 == 1:
        t3.write("사람2가 이겼습니다.")
    elif human2 == 2:
        t3.write("사람1이 이겼습니다.")
elif human1 == 1:
    if human2 == 0:
        t3.write("사람1이 이겼습니다.")
    elif human2 == 1:
        t3.write("무승부")
    elif human2 == 2:
        t3.write("사람2가 이겼습니다.")
elif human1 == 2:
    if human2 == 0:
        t3.write("사람2가 이겼습니다.")
    elif human2 == 1:
        t3.write("사람1이 이겼습니다.")
    elif human2 == 2:
        t3.write("무승부")    


