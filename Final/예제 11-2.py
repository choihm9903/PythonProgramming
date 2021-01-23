def list_avg(numlist):
    sum = 0
    for number in numlist:
        sum += number
    avg = sum/len(numlist)
    return avg

math_score = [90,80,70,60,50]
print(list_avg(math_score))
