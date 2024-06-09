import sys
from collections import defaultdict
t = sys.stdin.readline
n = int(t())
ls = defaultdict(list)
for i in range(n):
    b = t().strip()
    ls[b].append(i+1)

for x, y in sorted([(sum(ls[i])/len(ls[i]), i) for i in sorted(ls.keys())]):
    print(y)