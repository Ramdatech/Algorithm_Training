import sys
import math
t = sys.stdin.readline
n1 = int(t())
n2 = int(t())
a = set(x for x in range(n1,n2+1))
li = set(x for x in range(2,n2+1))
res = set()
while li :
    f = min(li)
    li.remove(f)
    li = set(li) - set(f*x for x in range(2,(n2//f)+2))
    res.add(f)
    if f >= math.sqrt(n2) :
        res |= li
        break

b = a & res
if len(b) > 0 :
    print(sum(b))
    print(min(b))
else :
    print(-1)