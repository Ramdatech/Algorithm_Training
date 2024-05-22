import sys
from itertools import zip_longest
t = sys.stdin.readline
n, m, s = map(int, t().split())
ls = zip_longest(*[sorted(list(map(int, t().strip().split())), reverse=True) for _ in range(3)], fillvalue=0)

r, e = 0, 0
for i in ls :
    e += sum(i)
    if 0 in i :
        r += sum(i)
    else :
        r += sum(i) * 9 // 10
print(e)
print(r)