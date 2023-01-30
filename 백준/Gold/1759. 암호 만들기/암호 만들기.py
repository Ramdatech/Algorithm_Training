import sys
from itertools import combinations, permutations
input = sys.stdin.readline
a, b = map(int, input().split())
ls = sorted(input().split())
t = set(['a', 'e', 'i', 'o', 'u'])
res = []
for i in sorted(combinations(ls, a)):
    if len(set(i) & t) >= 1 and len(set(i)-t) >= 2:
        print(''.join(i))