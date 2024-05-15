import sys
from collections import deque
t = sys.stdin.readline
n = int(t().strip())

que = deque([[n, 0]])
vst = set()
while que :
    x, cnt = que.popleft()
    if x == 1 :
        print(cnt)
        break
    if x in vst :
        continue
    vst.add(x)

    if x % 3 == 0 :
        que.append([x//3, cnt+1])
    if x % 2 == 0 :
        que.append([x//2, cnt+1])
    que.append([x-1, cnt+1])
