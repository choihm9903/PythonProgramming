import turtle
win = turtle.Screen()
t1 = turtle.Turtle()

def Giyuk():
    t1.fd(100)
    t1.rt(90)
    t1.fd(100)

def Nien():
    t1.bk(100)
    t1.lt(90)
    t1.fd(100)

character = input("ㄱ 또는 ㄴ 입력: ")

if character == "ㄱ":
    Giyuk()
elif character == "ㄴ":
    Nien()

while character != "ㄱ" and character != "ㄴ":
    if character == "ㄱ":
        Giyuk()
    elif character == "ㄴ":
        Nien()
    else:
        character = input("ㄱ 또는 ㄴ 다시입력: ")
        


  
