score = [90,80,70,60,50]

sum = 0
max = 0

for number in score:
    sum += number
    if number > max:
        max = number

average = sum/len(score)

if average >= 60:
    message = "Pass"
else:
    message = "Fail"

print("평균:",average,"\n가장 높은 시험 점수:",max,"\n",message,"입니다.")
    
