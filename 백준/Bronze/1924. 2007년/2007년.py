import sys
days = '0 31 28 31 30 31 30 31 31 30 31 30 31'.split()
days = list(map(int, days))
week = 'SUN MON TUE WED THU FRI SAT'.split()
input = sys.stdin.readline
m, d = map(int,input().split())
day = sum(days[:m]) + d
print(week[day%7])