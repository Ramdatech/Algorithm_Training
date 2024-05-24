import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, t().strip().split())) for _ in range(n)]
res = 0
for i in range(n):
    x1, x2 = ls[i]
    y1, y2 = ls[(i+1)%n]
    res += x1*y2 - x2*y1
print(abs(res)/2)