def calc(divide, num, res=0) :
    if num%divide != 0 :
        return res, num
    else :
        res, temp = calc(divide, num//divide, res)
        res += 1
    return res, temp


import sys
input = sys.stdin.readline
n = int(input().strip())
score = 0
for i in range(1, n+1):
    score, result = calc(10, i, score)
    score, result = calc(5, result, score)

print(score)