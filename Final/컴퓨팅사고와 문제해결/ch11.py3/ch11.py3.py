import turtle
win = turtle.Screen()
t1 = turtle.Turtle()
win.bgpic("11.maze.gif")

x1 = 108
y1 = -238
x2 = 168
y2 = -298
distance = 10

def getMinValue(v1, v2):
    if v1 < v2:
        return v1
    return v2

def getMaxValue(v1, v2):
    if v1 > v2:
        return v1
    return v2

def moveTo(x, y):
    t1.penup()
    t1.goto(x, y)
    t1.pendown()

def writeGameOver():
    t1.penup()
    t1.home()
    t1.pendown()
    t1.write("Game over")

def isInTrap(x, y, x1, y1, x2, y2):
    minX = getMinValue(x1, x2)
    maxX = getMaxValue(x1, x2)
    minY = getMinValue(y1, y2)
    maxY = getMaxValue(y1, y2)
    if x >= minX and x <= maxX and y >= minY and y <= maxY:
        return True
    else:
        return False

def showTrapInRed(x1, y1, x2, y2):
    t1.fillcolor("red")
    t1.begin_fill()
    moveTo(x1, y1)
    t1.goto(x2, y1)
    t1.goto(x2, y2)
    t1.goto(x1, y2)
    t1.goto(x1, y1)
    t1.end_fill()
    moveTo(x2 + distance, y2 + distance)

def checkTurtleInTrap(newx, newy):
    if isInTrap(newx, newy, x1, y1, x2, y2):
        showTrapInRed(x1, y1, x2, y2)
        writeGameOver()

def keyeast():
    position = t1.pos()
    t1.goto(position[0] + distance, position[1])
    checkTurtleInTrap(position[0] + distance, position[1])
  
def keywest():
    position = t1.pos()
    t1.goto(position[0] - distance, position[1])
    checkTurtleInTrap(position[0] - distance, position[1])

def keysouth():
    position = t1.pos()
    t1.goto(position[0], position[1] - distance)
    checkTurtleInTrap(position[0], position[1] - distance)

def keynorth():
    position = t1.pos()
    t1.goto(position[0], position[1] + distance)
    checkTurtleInTrap(position[0], position[1] + distance)

win.onkey(keyeast, 'Right')
win.onkey(keywest, 'Left')
win.onkey(keysouth, 'Down')
win.onkey(keynorth, 'Up')

win.listen()
turtle.mainloop()
