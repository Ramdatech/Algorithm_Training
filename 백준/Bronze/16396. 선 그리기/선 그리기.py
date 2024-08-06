import sys
t = sys.stdin.readline
ls = [False]*10001
for _ in range(int(t())):
    n, m = map(int, t().split())
    for i in range(n, m):
        if not ls[i]:
            ls[i] = True
print(sum(ls))