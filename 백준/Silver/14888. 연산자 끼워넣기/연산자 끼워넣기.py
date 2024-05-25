import sys
from collections import deque
t = sys.stdin.readline
n = int(t())
ls = list(map(int, t().split()))
c1, c2, c3, c4 = list(map(int, t().split()))

que = deque([(0, ls[0], (0, 0, 0, 0))])
mx, mn = -1e12, 1e12
while que:
    cnt, num, (a, b, c, d) = que.popleft()
    if (a, b, c, d) == (c1, c2, c3, c4):
        mx = max(mx, num)
        mn = min(mn, num)
    if a < c1:
        que.append((cnt+1, num+ls[cnt+1], (a+1, b, c, d)))
    if b < c2:
        que.append((cnt+1, num-ls[cnt+1], (a, b+1, c, d)))
    if c < c3:
        que.append((cnt+1, num*ls[cnt+1], (a, b, c+1, d)))
    if d < c4 and num < 0 :
        que.append((cnt+1, -(-num//ls[cnt+1]), (a, b, c, d+1)))
    elif d < c4 :
        que.append((cnt+1, num//ls[cnt+1], (a, b, c, d+1)))
print(mx)
print(mn)