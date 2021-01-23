def drawDigeud(size):
    t1.penup()
    t1.home()
    t1.pendown()
    t1.clear()
    t1.backward(size)
    t1.right(90)
    t1.forward(size)
    t1.left(90)
    t1.forward(size)


# 원래 크기
import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

drawDigeud(100)

# 'ㄷ'자를 1/4배로 
# 그림. 가로와 세로 
# 길이를 1/2로 줄임

drawDigeud(50)

# 'ㄷ'자를 4배로 그림 
# 가로와 세로 길이를 원래 
# 길이의 두 배로 늘림
size = 200
drawDigeud(size)