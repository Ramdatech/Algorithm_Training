import sys
from itertools import product
t = sys.stdin.readline
a, b = map(int, t().split())
print('\n'.join([' '.join(i) for i in product(map(str,sorted(list(map(int, t().split())))), repeat=b)]))