import sys
t = sys.stdin.readline
for _ in range(int(t())):
    a,c,b = map(int, t().split())
    print(a*(b-1)+c)