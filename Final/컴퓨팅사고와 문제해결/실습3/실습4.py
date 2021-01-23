import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def addDiceImages():
    for i in range(6):
        win.addshape("dice"+str(i+1)+".gif")

def moveTo(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()

def showDiceImage(x, y, num):
    moveTo(x,y)
    t1.shape("dice"+str(num)+".gif")
    t1.stamp()
    t1.shape("turtle")

def writeText(x, y, text):
    moveTo(x, y)
    t1.write(text)

n1 = int(input("1-6까지의 숫자중 하나 입력: "))
import random
n2 = random.randint(1,6)

while n1 == n2:
    n2 = random.randint(1,6)

addDiceImages()
showDiceImage(-200,0,n1)
showDiceImage(200,0,n2)
writeText(-220,200,"사람")
writeText(180,200,"컴퓨터")

if n1 > n2:
    writeText(-50,-200,"사람이 이겼습니다.")
elif n1 < n2:
    writeText(-50,-200,"컴퓨터가 이겼습니다.")

moveTo(0,0)
