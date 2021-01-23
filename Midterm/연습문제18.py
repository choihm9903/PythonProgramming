print('1부터 10까지의 정수 중 행운의 숫자와 한국인이 좋아하는 숫자를 입력하시오.')
num1 = int(input('행운의 숫자 '))
num2 = int(input('한국인이 좋아하는 숫자 '))

if num1 == 7:
    if num2 == 3:
        print('둘 다 정답')
    else:
        print('행운의 숫자만 정답')
else:
    if num2 == 3:
        print('한국인이 좋아하는 숫자만 정답')
    else:
        print('둘 다 오답')

           
