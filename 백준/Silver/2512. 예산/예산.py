import sys
import bisect
t = sys.stdin.readline
n = int(t())
ls = sorted(list(map(int, t().split())))
m = int(t())
if sum(ls) <= m :
    print(ls[-1])
else :
    a, b = 0, max(ls)
    while a < b :
        mid = (a+b+1)//2
        if sum([mid if i > mid else i for i in ls]) <= m :
            a = mid
        else :
            b = mid - 1
    print(a)