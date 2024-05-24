import sys
from itertools import permutations
t = sys.stdin.readline
n, m = map(int, t().strip().split())
ls = sorted(list(set(map(int, t().strip().split()))))
n = len(ls)
res = set()

def recur(idx, cnt, s):
    if cnt == m:
        res.add(tuple(s))
        return
    for i in range(idx, n):
        recur(i, cnt + 1, s + [ls[i]])

recur(0, 0, [])
for i in sorted(list(res)) :
    print(*i)