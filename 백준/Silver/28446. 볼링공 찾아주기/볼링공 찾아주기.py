import sys
t = sys.stdin.readline
n = int(t())
d = {}
for i in range(n):
    c, *b = map(int, t().split())
    if c == 1 : 
        d[b[1]] = b[0]
    if c == 2 : 
        print(d[b[0]])