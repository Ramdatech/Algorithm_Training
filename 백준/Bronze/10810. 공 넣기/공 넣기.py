import sys
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [0]*n
for i in range(m) :
    a, b, c = map(int, t().split())
    ls = ls[:a-1] + [c]*(b-a+1) + ls[b:]
print(*ls)