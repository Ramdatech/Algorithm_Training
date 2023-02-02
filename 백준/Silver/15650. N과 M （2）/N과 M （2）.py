import sys
from itertools import combinations
t = sys.stdin.readline
a, b = map(int, t().split())
print(*[' '.join(i) for i in combinations([str(x) for x in range(1, a+1)], b)], sep='\n')