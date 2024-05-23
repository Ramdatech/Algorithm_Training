import sys
from itertools import permutations
t = sys.stdin.readline
n, m = map(int, t().strip().split())
ls = list(map(int, t().strip().split()))
for i in sorted(list(set(permutations(ls, m)))) :
    print(*i)