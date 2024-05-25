import sys
t = sys.stdin.readline
n = int(t())
r = set()
res = 0
for i in range(n):
    a = t().strip()
    if a == "ENTER":
        res += len(r)
        r = set()
    else :
        r.add(a)
else :
    res += len(r)
print(res)