def price():
    sum = 0
    place = input("춘천(운임 : 5000원) 부산(운임 :30000원) 대구(운임 20000원) 수원(운임 10000) 중 목적지를 한곳 입력하세요 : ")
    train = input("KTX(10000원 추가) / 새마을호(5000원 추가) / 무궁화호(3000원 추가) 중 하나를 입력하세요: ")
    seat = input("좌석 / 입석(2000원 할인)중 하나를 입력하세요: ")

    if place == "춘천":
        sum += 5000
    elif place == "부산":
        sum += 30000
    elif place == "대구":
        sum += 20000
    else:
        sum += 10000

    if train == "KTX":
        sum += 10000
    elif train == "새마을호":
        sum += 5000
    else:
        sum += 3000

    if seat == "입석":
        sum -= 2000

    return sum

print(price(),"원")
