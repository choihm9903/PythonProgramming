num1 = int(input('양의 정수1을 입력하시오. '))
num2 = int(input('양의 정수2을 입력하시오. '))
num3 = int(input('양의 정수3을 입력하시오. '))
sum = num1+num2+num3

if sum%2 == 0:
    if num1 >= num2:
        max = num1
        if num1 >= num3:
            print('합은 짝수, 가장 큰 수는', max,'입니다.')
        else:
            max = num3
            print('합은 짝수, 가장 큰 수는', max,'입니다.')
    else:
        max = num2
        if num2 >= num3:
            print('합은 짝수, 가장 큰 수는', max,'입니다.')
        else:
            max = num3
            print('합은 짝수, 가장 큰 수는', max,'입니다.')
else:
    print('합은 홀수, 합은', sum,'입니다.')
