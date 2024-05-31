import sys
t = sys.stdin.readline
n = int(t())
for _ in range(n):
    print(sorted([[int(x) if x.isdecimal() else x for x in t().strip().split()] for _ in range(int(t()))], key=lambda x: x[1])[-1][0])