def elevator():
    inputLocation = int(input("가고자 하는 층 입력: "))
    nowLocation = int(input("현배 위치 입력: "))

    while (inputLocation == nowLocation) or not (1 <= inputLocation <= 6):
        print("다른 층(1~6)을 입력해주세요.")
        inputLocation = int(input("가고자 하는 층 입력: "))
        nowLocation = int(input("현배 위치 입력: "))

    if inputLocation > nowLocation:
        while inputLocation >= nowLocation:
            print("현재 층은 ",nowLocation,"입니다.")
            nowLocation += 1
    else:
        while inputLocation <= nowLocation:
            print("현재 층은 ",nowLocation,"입니다.")
            nowLocation -= 1
    print(inputLocation,"층에 도착하였습니다. 안녕히 가세요")

elevator()
