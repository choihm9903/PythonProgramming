num1 = int(input('양의 정수1을 입력하시오. '))
num2 = int(input('양의 정수2을 입력하시오. '))
num3 = int(input('양의 정수3을 입력하시오. '))

if num1 >= num2:
    max = num1
    if max >= num3:
        print('가장 큰 수는 ',max,'입니다.')
    else:
            max = num3
            print('가장 큰 수는 ',max,'입니다.')
else:
    max = num2
    if max >= num3:
        print('가장 큰 수는 ',max,'입니다.')
    else:
        max = num3
        print('가장 큰 수는 ',max,'입니다.')
