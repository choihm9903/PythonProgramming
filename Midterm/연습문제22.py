x1 = int(input('점1의 x좌표를 입력하시오. '))
y1 = int(input('점1의 y좌표를 입력하시오. '))
x2 = int(input('점2의 x좌표를 입력하시오. '))
y2 = int(input('점2의 y좌표를 입력하시오. '))

if x1 <= x2:
    x = x2-x1
    if y1 <= y2:
        y = y2-y1
    else:
        y = y1-y2
else:
    x = x1-x2
    if y1 <= y2:
        y = y2-y1
    else:
        y = y1-y2

length = (x**2 + y**2)**0.5
print('두 점 사이의 거리는', length,'입니다.')
