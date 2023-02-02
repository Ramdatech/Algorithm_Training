import sys
from itertools import combinations
t = sys.stdin.readline
a, b = map(int, t().split())
for i in combinations([x for x in range(1, a+1)], b) :
    print(*i)