import sys
from itertools import combinations
t = sys.stdin.readline
for i in combinations([int(t()) for _ in range(9)], 7):
    if sum(i) == 100 :
        print(*sorted(list(i)), sep='\n')
        break