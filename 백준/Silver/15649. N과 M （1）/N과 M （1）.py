import sys
from itertools import permutations
t = sys.stdin.readline
a, b = map(int, t().split())
print('\n'.join([' '.join(i) for i in permutations([str(x) for x in range(1, a+1)], b)]))