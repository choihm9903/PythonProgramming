import random

def writeResult(value, human):
    if value == 0:
        print(human, "가위")
    elif value == 1:
        print(human, "바위")
    else:
        print(human, "보")
    
human1 = random.randint(0, 2)
human2 = random.randint(0, 2)
writeResult(human1, "사람1")
writeResult(human2, "사람2")
if human1 == 0 and human2 == 0:
    print("무승부")
elif human1 == 0 and human2 == 1:
    print("사람2가 이겼습니다.")
elif human1 == 0 and human2 == 2:
    print("사람1이 이겼습니다.")
elif human1 == 1 and human2 == 0:
    print("사람1이 이겼습니다.")
elif human1 == 1 and human2 == 1:
    print("무승부")
elif human1 == 1 and human2 == 2:
    print("사람2가 이겼습니다.")
elif human1 == 2 and human2 == 0:
    print("사람1이 이겼습니다.")
elif human1 == 2 and human2 == 1:
    print("사람2가 이겼습니다.")
elif human1 == 2 and human2 == 2:
    print("무승부")    
