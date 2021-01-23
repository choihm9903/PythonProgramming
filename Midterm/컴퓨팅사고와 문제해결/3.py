math = float(input('수학 성적을 입력하시오.'))
english = float(input('영어 성적을 입력하시오.'))
korean = float(input('국어 성적을 입력하시오.'))
average = (math + english + korean)/3

if math > 60.5 and english > 60.5 and korean > 60.5 or average >= 70.8:
    print('자격증을 딸 수 있습니다.')
else:
    print('자격증을 딸 수 없습니다.')
