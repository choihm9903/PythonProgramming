def security():
    password = input("비밀번호 입력: ")
    if len(password) >= 9:
        print("Good")
    elif len(password) < 5:
        print("Bad")
    else:
        print("Normal")

security()
