import sys
import math
t = sys.stdin.readline
n1, n2 = map(int, t().split())
a = set(x for x in range(n1,n2+1))
li = set(x for x in range(2,n2+1))
res = set()


while 1 :
    f = min(li)
    li.remove(f)
    li = set(li) - set(f*x for x in range(2,(n2//f)+1))
    res.add(f)
    if f >= math.sqrt(n2) :
        res |= li
        break

b = sorted(a & res)
for i in b:
    print(i)