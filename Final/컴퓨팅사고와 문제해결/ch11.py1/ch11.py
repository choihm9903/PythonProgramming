import turtle
win = turtle.Screen()
playerTurtle = turtle.Turtle()
computerTurtle = turtle.Turtle()

win.setup(700, 600)
win.addshape("scissors.gif")
win.addshape("rock.gif")
win.addshape("paper.gif")

playerTurtle.penup()
playerTurtle.goto(-180, 0)
playerTurtle.pendown()
computerTurtle.penup()
computerTurtle.goto(180, 0)
computerTurtle.pendown()

def checkWhoWins(p, c):
    if p == 1:
        if c == 1:
            print("무승부")
        elif c == 2:
            print("컴퓨터가 이겼습니다")
        elif c == 3:
            print("사람이 이겼습니다")
    elif p == 2:
        if c == 1:
            print("사람이 이겼습니다")
        elif c == 2:
            print("무승부")
        elif c == 3:
            print("컴퓨터가 이겼습니다")
    elif p == 3:
        if c == 1:
            print("컴퓨터가 이겼습니다")
        elif c == 2:
            print("사람이 이겼습니다")
        elif c == 3:
            print("무승부")

def showPlayerImage(player):
    if player == 1:
        playerTurtle.shape("scissors.gif")
    elif player == 2:
        playerTurtle.shape("rock.gif")
    elif player == 3:
        playerTurtle.shape("paper.gif")

def showComputerImage(computer):
    if computer == 1:
        computerTurtle.shape("scissors.gif")
    elif computer == 2:
        computerTurtle.shape("rock.gif")
    elif computer == 3:
        computerTurtle.shape("paper.gif")

def playGame(player):
    showPlayerImage(player)
    import random
    computer = random.randint(1, 3)
    showComputerImage(computer)
    checkWhoWins(player, computer)

def playGameWithScissors():
    playGame(1)

def playGameWithRock():
    playGame(2)

def playGameWithPaper():
    playGame(3)

win.onkey(playGameWithScissors, 's')
win.onkey(playGameWithScissors, 'S')
win.onkey(playGameWithRock, 'r')
win.onkey(playGameWithRock, 'R')
win.onkey(playGameWithPaper, 'p')
win.onkey(playGameWithPaper, 'P')

win.listen()
turtle.mainloop()
