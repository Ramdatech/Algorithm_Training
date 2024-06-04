import sys
from collections import deque
t = sys.stdin.readline
F, S, G, U, D = map(int, t().split())
if S == G:
    print(0)
    sys.exit()
vst = [0]*(F+1)
vst[S] = 1
que = deque([(S, 0)])
while que:
    cur, cnt = que.popleft()
    for nxt in [cur+U, cur-D]:
        if 1 <= nxt <= F and not vst[nxt]:
            if nxt == G:
                print(cnt+1)
                sys.exit()
            vst[nxt] = 1
            que.append((nxt, cnt+1))
print('use the stairs')