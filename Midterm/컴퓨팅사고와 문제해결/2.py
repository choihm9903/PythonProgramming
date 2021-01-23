a=int(input('사과 개수를 입력하시오. '))
b=int(input('포도 개수를 입력하시오. '))
c=int(input('배 개수를 입력하시오. '))
d=int(input('귤 개수를 입력하시오. '))
total_price=a*1000+b*3000+c*2000+d*500
if b>=3 or a>=2:
    total_price=total_price*0.9
    print('10% 할인되었습니다.')
    print('총 금액은',total_price,'원 입니다.')
else:
    print('총 금액은',total_price,'원 입니다.')
