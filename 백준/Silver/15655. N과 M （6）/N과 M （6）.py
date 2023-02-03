import sys
from itertools import combinations
t = sys.stdin.readline
a, b = map(int, t().split())
print('\n'.join([' '.join(i) for i in combinations(map(str,sorted(list(map(int, t().split())))), b)]))