import sys
t = sys.stdin.readline
n = int(t())
ls = sorted([int(t()) for _ in range(n)])[::-1]
res = -1
for i in range(1, n+1):
    tmp = ls[i-1] * i
    res = max(res, tmp)
print(res)