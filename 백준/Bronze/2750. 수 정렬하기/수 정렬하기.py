import sys
t = sys.stdin.readline
a = int(t())
res = []
for i in range(a):
    res.append(int(t()))
res = sorted(res)
for i in res:
    print(i)