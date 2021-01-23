def PassFail(scorelist):
    sum = 0
    for score in scorelist:
        sum += score
    average = sum/len(scorelist)

    if average >= 60:
        print("pass")
    else:
        print("fail")

PassFail([30,40,50,60,70])
