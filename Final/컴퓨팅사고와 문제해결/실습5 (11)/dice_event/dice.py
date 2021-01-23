import random
import turtle
win = turtle.Screen()
t1 = turtle.Turtle()


    
def rollDiceXY(x, y):
    if x >= -160 and x <= 160 and y >= -160 and y <= 160:
        rollDice()
    
def rollDice():
    dicenum = random.randint(1, 6)
    print("dicenum = ", dicenum)
    t1.shape("dice" + str(dicenum) + ".gif")
    #t1.stamp()
    """
    if dicenum == 1:
        t1.shape("dice1.gif")
    elif dicenum == 2:
        t1.shape("dice2.gif")
    elif dicenum == 3:
        t1.shape("dice3.gif")
    elif dicenum == 4:
        t1.shape("dice4.gif")
    elif dicenum == 5:
        t1.shape("dice5.gif")
    elif dicenum == 6:
        t1.shape("dice6.gif")
    """

#win.addshape("dice1.gif")
#win.addshape("dice2.gif")
#win.addshape("dice3.gif")
#win.addshape("dice4.gif")
#win.addshape("dice5.gif")
#win.addshape("dice6.gif")
for i in range(1, 7):
    win.addshape("dice" + str(i) + ".gif")

win.onkey(rollDice, 'r')
win.onkey(rollDice, 'R')
win.onkey(turtle.bye, 'q')
win.onkey(turtle.bye, 'Q')
win.onclick(rollDiceXY)

win.listen()
turtle.mainloop()

#ch = input("r, R, q, Q 중 한 개를 입력하세요:")
#while True:
#    if ch == 'r' or ch == 'R':
#        rollDice()
#    elif ch == 'q' or ch == 'Q':
#        print("quit")
#        # 종료 ....
#        break
#    ch = input("r, R, q, Q 중 한 개를 입력하세요:")
#print("end")
