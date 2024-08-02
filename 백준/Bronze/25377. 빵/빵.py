import sys
t = sys.stdin.readline
n = int(t())
mn = 1e9
for _ in range(n):
    a, b = map(int, t().split())
    if a <= b :
        mn = min(mn, b)
else :
    print(-1 if mn == 1e9 else mn)