period = input('출국 전 남은 기간을 입력하시오.(1달 전/1달반 전) ')
country = input('여행할 국가를 입력하시오.(영국/프랑스/독일/그리스) ')

if period == '1달전':
    if country == '영국':
        charge = 70
    elif country == '프랑스':
        charge = 67
    elif country == '독일':
        charge = 63
    elif country == '그리스':
        charge = 60

    charge = charge*0.97
    print('비행기 표 가격은 3% 할인되어 ',charge,'만원 입니다.')

else:
    if country == '영국':
        charge = 70
    elif country == '프랑스':
        charge = 67
    elif country == '독일':
        charge = 63
    elif country == '그리스':
        charge = 60

    charge = charge*0.95
    print('비행기 표 가격은 5% 할인되어 ',charge,'만원 입니다.')
    
        
