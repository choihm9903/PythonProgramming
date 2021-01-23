def score(score_list):
    print("학생들의 점수는 ",score_list,"점 입니다.")
    num = int(input("1.평균 2.최고점 3.최저점: "))
    if num == 1:
        sum = 0
        for score in score_list:
            sum += score
        average = sum/len(score_list)
        print("평균 점수: ",average)
    elif num == 2:
        score = max(score_list)
        print("최고점: ",score)
    else:
        score = min(score_list)
        print("최저점: ",score)

score([95,90,45,10,80,100])
