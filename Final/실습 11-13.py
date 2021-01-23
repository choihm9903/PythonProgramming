def calculator():
    print("***계산기***")
    cal_type = int(input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료:"))
    while (cal_type < 5):
        n1 = float(input("정수 2개 입력: \n"))
        n2 = float(input(""))
        if cal_type == 1:
            sum = n1 + n2
        elif cal_type == 2:
            if n1 >= n2:
                sum = n1 - n2
            else:
                sum = n2 - n1
        elif cal_type == 3:
            sum = n1 * n2
        else:
            sum = n1 / n2
        print("결과: ",sum)
        cal_type = int(input("1.덧셈 2.뺄셈 3.곱셈 4.나눗셈 5.종료:"))

calculator()
