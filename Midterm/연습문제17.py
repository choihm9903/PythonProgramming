num1 = int(input('양의 정수1을 입력하시오. '))
num2 = int(input('양의 정수2을 입력하시오. '))
total=num1+num2
if total%2 == 0:
         if total%3 == 0:
             print('합은 짝수이며 3의 배수이다.')
         else:
             print('합은 짝수이며 3의 배수는 아니다.')
else:
         if total%3 == 0:
             print('합은 홀수이며 3의 배수이다.')
         else:
             print('합은 홀수이며 3의 배수는 아니다.')
