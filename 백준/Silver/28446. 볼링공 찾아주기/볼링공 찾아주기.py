import sys
t = sys.stdin.readline
n, d = int(t()), {}
for _ in range(n):
    a, b, *c = map(int, t().split())
    if c : d[c[0]] = b
    else : print(d[b])