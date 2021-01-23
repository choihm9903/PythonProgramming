factorial = 1
num1 = 1
num2 = int(input('정수를 입력하시오. '))

while(num1 <= num2):
    factorial =  factorial * num1
    num1 += 1
    

print(num2,'! =',factorial)
