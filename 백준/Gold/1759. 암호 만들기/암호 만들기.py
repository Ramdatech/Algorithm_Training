import sys
from itertools import combinations, permutations

input = sys.stdin.readline
a, b = map(int, input().split())
ls = sorted(input().split())
res = []
for i in sorted(combinations(ls, a)):
    if len(set(i) & set(['a', 'e', 'i', 'o', 'u'])) >= 1 and len(set(i)-set(['a', 'e', 'i', 'o', 'u'])) >= 2:
        res.append(''.join(i))
res.sort()
for i in res :
    print(i)