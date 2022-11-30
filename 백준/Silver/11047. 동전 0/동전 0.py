import sys
input = sys.stdin.readline
n, m = map(int,input().split())
answer = 0
money = sorted([int(input().strip()) for i in range(n)], reverse=True)
for i in money :
    if m//i > 0 :
        answer += m//i
        m = m%i
print(answer)