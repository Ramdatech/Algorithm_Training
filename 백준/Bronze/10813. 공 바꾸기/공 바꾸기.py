import sys
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [x for x in range(n+1)]
for i in range(m) :
    a, b = map(int, t().split())
    ls[a],ls[b] = ls[b], ls[a]
print(*ls[1:])