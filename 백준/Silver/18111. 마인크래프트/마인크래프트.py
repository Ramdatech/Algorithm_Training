import sys
input = sys.stdin.readline
n, m, b = map(int,input().split())
ls = []
for i in range(n) :
    temp = list(map(int, input().split()))
    ls += temp
answer = [10e10, -1]
goal = int(round(sum(ls)/len(ls), 0)) # 목표층수
for i in range(max(ls), -1, -1) :
    temp_second = 0
    temp_inventory = b
    for tempvar in ls :
        if i > tempvar : #목표보다 현재 블럭이 작으므로,
            temp_second += abs(i-tempvar) #설치한다.
            temp_inventory -= abs(i-tempvar)
        elif i < tempvar : #목표보다 현재 블럭이 많으므로,
            temp_second += abs(i-tempvar)*2 #캐낸다.
            temp_inventory += abs(i-tempvar)
    if temp_second >= 0 and temp_inventory >= 0 and temp_second < answer[0]:
        answer = [temp_second, i]
answer = [0, 0] if answer[1] == -1 else answer
print(*answer)