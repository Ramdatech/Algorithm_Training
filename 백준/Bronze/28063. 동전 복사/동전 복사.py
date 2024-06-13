import sys
from collections import deque, defaultdict
t = sys.stdin.readline
n = int(t())
w, h = map(int, t().split())
print(sum([1 for x in [w, h] for y in [1, n] if x!=y]))