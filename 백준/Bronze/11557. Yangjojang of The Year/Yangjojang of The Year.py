import sys
t = sys.stdin.readline
n = int(t())
for _ in range(n):
    m = int(t())
    tmp = sorted([[int(x) if x.isdecimal() else x for x in t().strip().split()] for _ in range(m)], key=lambda x: x[1])
    print(tmp[-1][0])