def price():
    totalPrice = int(input("소비자가 입력(원): "))
    productPrice = totalPrice*(10/11)
    tax = totalPrice/11
    print("제품 가격은 ",productPrice,"부가가치세는 ",tax,"원입니다.")

price()
