import sys
from itertools import permutations
t = sys.stdin.readline
a, b = map(int, t().split())
a = map(str,sorted(list(map(int, t().split()))))
print('\n'.join([' '.join(i) for i in permutations(a, b)]))