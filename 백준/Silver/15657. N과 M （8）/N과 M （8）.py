import sys
from itertools import combinations_with_replacement
t = sys.stdin.readline
a, b = map(int, t().split())
print('\n'.join([' '.join(i) for i in combinations_with_replacement(map(str,sorted(list(map(int, t().split())))), b)]))