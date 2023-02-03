import sys
from itertools import combinations
t = sys.stdin.readline
a, b = map(int, t().split())
a = map(str,sorted(list(map(int, t().split()))))
print('\n'.join([' '.join(i) for i in combinations(a, b)]))