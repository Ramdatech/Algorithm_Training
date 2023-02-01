import sys
from itertools import combinations
t = sys.stdin.readline
a, b = map(int, t().split())
ls = list(map(int, t().split()))
res = 0
for i in range(1, a+1):
    temp = combinations(ls, i)
    for i in temp :
        if sum(i) == b :
            res += 1
print(res)