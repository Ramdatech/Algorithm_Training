import sys
t = sys.stdin.readline
n = int(t())
tmp = [[x, x] for x in list(map(int, t().strip().split()))]
for _ in range(0, n-1) :
    a = list(map(int, t().strip().split()))
    s = [[z for z in [j-1, j, j+1] if 0 <= z < 3] for j in range(3)]
    s = [[[tmp[j][0] for j in i] for i in s], [[tmp[j][1] for j in i] for i in s]]
    tmp = [[a[t] + max(s[0][t]), a[t] + min(s[1][t])] for t in range(3)]

mx, mn = -1e12, 1e12
for x, y in tmp:
    mx = max(mx, x)
    mn = min(mn, y)
print(mx, mn)