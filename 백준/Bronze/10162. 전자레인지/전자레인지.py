import sys
t = sys.stdin.readline
n = int(t())
res = []
for i in [300, 60, 10]:
    res.append(n // i)
    n %= i
if n == 0:
    print(*res)
else:
    print(-1)