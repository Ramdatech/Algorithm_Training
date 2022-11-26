import sys
t = sys.stdin.readline
n, k = map(int, t().split())
res = sorted(list(map(int, t().split())))[::-1]
print(res[k-1])