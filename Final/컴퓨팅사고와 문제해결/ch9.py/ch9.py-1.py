import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

for i in range(5):
    win.addshape("dice"+str(i+1)+".gif")
    
import random
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
elif n == 6:
    t1.shape("dice6.gif")

t1.stamp()
t1.shape("turtle")
    
