import sys
from collections import deque

t = sys.stdin.readline
a, b = map(int, t().strip().split())

que = deque([(a, 0)])
vst = set()
while que :
    x, cnt = que.popleft()
    if x == b :
        print(cnt)
        break
    if x in vst :
        continue
    vst.add(x)

    if x < 100000 :
        que.append((x+1, cnt+1))
    if x >= 1 :
        que.append((x-1, cnt+1))
    if x <= 50000 :
        que.append((2*x, cnt+1))