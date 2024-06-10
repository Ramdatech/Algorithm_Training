import sys
t = sys.stdin.readline
n, m = map(int, t().strip().split())
w, h = zip(*[list(map(int, t().strip().split())) for _ in range(m)])
w, h = sorted(w), sorted(h)
res = 0
for i in range(m) :
    res += abs(w[m//2] - w[i]) + abs(h[m//2] - h[i])
print(res)