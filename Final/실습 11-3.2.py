def average(scorelist):
    sum = 0
    for score in scorelist:
        sum += score
    return score/len(scorelist)

def PassFail(scorelist):
    if average(scorelist) >= 60:
        message = "Pass"
    else:
        message = "Fail"
    return message

print(PassFail([30,40,50,60,70]))
