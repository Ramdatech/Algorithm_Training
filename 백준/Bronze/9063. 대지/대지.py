import sys
t = sys.stdin.readline
n = int(t().strip())
x, y = zip(*[list(map(int, t().split())) for _ in range(n)])
print((max(x)-min(x))*(max(y)-min(y)))