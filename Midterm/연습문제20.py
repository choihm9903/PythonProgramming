num1 = int(input('양의 정수1을 입력하시오. '))
num2 = int(input('양의 정수2을 입력하시오. '))
num3 = int(input('양의 정수3을 입력하시오. '))

if num1 <= num2:
    min = num1
    if min <= num3:
        print('가장 작은 수는', min,'입니다.')
    else:
            min = num3
            print('가장 작은 수는', min,'입니다.')
else:
    min = num2
    if min <= num3:
        print('가장 작은 수는', min,'입니다.')
    else:
        min = num3
        print('가장 작은 수는', min,'입니다.')
