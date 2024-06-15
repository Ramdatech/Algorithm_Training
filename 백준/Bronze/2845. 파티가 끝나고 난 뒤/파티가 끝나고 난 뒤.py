import sys
t = sys.stdin.readline
n, m = map(int, t().split())
ls = list(map(int, t().strip().split()))
print(*[x-(n*m) for x in ls])