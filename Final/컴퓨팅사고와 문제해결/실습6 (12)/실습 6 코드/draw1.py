import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

first = True
positions = []

def mousegoto(x, y):
    global first
    if first:
        t1.penup()
        t1.goto(x, y)
        t1.pendown()
        first = False
    else:
        t1.goto(x, y)
    positions.append(x)
    positions.append(y)
    print(positions)
    
def mousegoto2(x, y):
    if len(positions) > 2:
        t1.goto(x, y)
        positions.append(x)
        positions.append(y)  
        t1.goto(positions[0], positions[1])
        positions.append(positions[0])
        positions.append(positions[1])  
    
def key1():
    t1.clear()
    for i in range(0, len(positions), 2):
        t1.goto(positions[i], positions[i + 1])
    
win.onclick(mousegoto)
win.onclick(mousegoto2, 3)
win.onkey(key1, 'r')
win.onkey(key1, 'R')

win.listen()
turtle.mainloop()
