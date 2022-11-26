import sys
t = sys.stdin.readline
n = int(t())
res = set()
for _ in range(n):
    a = t().strip()
    res.add(a)
for i in sorted(list(res), key = lambda x : (len(x), x)) :
    print(i)