import sys
a, b = map(int, sys.stdin.readline().split())
score = 0
res = 0
for i in range(1, a+1):
    if a%i == 0 :
        score += 1
        if b == score :
            res = i
print(res)