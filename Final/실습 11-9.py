def time():
    time = int(input("초 입력: "))
    hour = time // 3600
    minute = (time % 3600) // 60
    second = time % 60
    print(hour,"시 ",minute,"분",second,"초 입니다")

time()
    
