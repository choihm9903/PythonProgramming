import random
import turtle
win = turtle.Screen()
humanTurtle = turtle.Turtle()
computerTurtle = turtle.Turtle()
textTurtle = turtle.Turtle()

# 가위바위보 이미지 등록
win.addshape("rock.gif")
win.addshape("scissors.gif")
win.addshape("paper.gif")

def writeResult(human, computer):
    textTurtle.penup()
    textTurtle.goto(-40, -200)
    textTurtle.clear()
    if human == 0: # 가위
        if computer == 0: # 가위
            textTurtle.write("무승부")
        elif computer == 1: # 주먹 
            textTurtle.write("컴퓨터가 이겼습니다.")
        elif computer == 2: # 보자기 
            textTurtle.write("사람이 이겼습니다.")
    elif human == 1: # 주먹 
        if computer == 0:
            textTurtle.write("사람이 이겼습니다.")
        elif computer == 1:
            textTurtle.write("무승부")
        elif computer == 2:
            textTurtle.write("컴퓨터가 이겼습니다.")
    elif human == 2:
        if computer == 0:
            textTurtle.write("컴퓨터가 이겼습니다.")
        elif computer == 1:
            textTurtle.write("사람이 이겼습니다.")
        elif computer == 2:
            textTurtle.write("무승부")    
    
def processComputer():
    computerTurtle.penup()
    computerTurtle.goto(200, 0)
    computerTurtle.pendown()
    computer = random.randint(0, 2)
    if computer == 0:
        computerTurtle.shape("scissors.gif")
    elif computer == 1:
        computerTurtle.shape("rock.gif")
    else:
        computerTurtle.shape("paper.gif")
    return computer

def processHuman(shapeName, num):
    humanTurtle.penup()
    humanTurtle.goto(-200, 0)
    humanTurtle.pendown()
    c = processComputer()
    humanTurtle.shape(shapeName)
    writeResult(num, c)
    
def processHumanR():
    processHuman("rock.gif", 1)
 
def processHumanS():
    processHuman("scissors.gif", 0)
   
def processHumanP():
    processHuman("paper.gif", 2)


win.onkey(processHumanR, 'r')
win.onkey(processHumanR, 'R')
win.onkey(processHumanS, 's')
win.onkey(processHumanS, 'S')
win.onkey(processHumanP, 'p')
win.onkey(processHumanP, 'P')

win.listen()
turtle.mainloop()
