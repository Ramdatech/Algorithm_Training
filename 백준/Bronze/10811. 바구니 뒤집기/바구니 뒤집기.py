import sys
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [x for x in range(n+1)]
for i in range(m) :
    a, b = map(int, t().split())
    ls = ls[:a] + ls[a:b+1][::-1] + ls[b+1:]
print(*ls[1:])