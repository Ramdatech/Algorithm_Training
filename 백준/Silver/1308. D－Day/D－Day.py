def year_to_day(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

import sys
input = sys.stdin.readline
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
y1,m1,d1 = map(int, input().split())
y2,m2,d2 = map(int, input().split())

a = (y1+1000)*1000 + m1*100 + d1
b = (y2)*1000 + m2*100 + d2
if a <= b :
    print('gg')
else :
    total_day_1 = 365-sum(days[m1:])+d1
    total_day_2 = -sum(days[m2:])+d2
    if year_to_day(y1) and m1>2 :
        total_day_1 += 1
    if year_to_day(y2) and m2<3 :
        total_day_2 -= 1
    for i in range(y1, y2+1):
        if year_to_day(i) :
            total_day_2 += 366
        else :
            total_day_2 += 365
    print(f'D-{total_day_2 - total_day_1}')