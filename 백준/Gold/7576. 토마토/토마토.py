import sys
from collections import deque

t = sys.stdin.readline
m, n = map(int, t().strip().split())
ls = [list(map(int, t().strip().split())) for _ in range(n)]
pos = [(i, j, 0) for i in range(n) for j in range(m) if ls[i][j] == 1]
zero = set([(i, j) for i in range(n) for j in range(m) if ls[i][j] == 0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

que = deque(pos)
res = -1
while que :
    x, y, d = que.popleft()
    if res < d : res = d
    zero.discard((x, y))
    for i in range(4) :
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 0 :
            ls[nx][ny] = 1
            que.append((nx, ny, d+1))

if zero :
    print(-1)
else :
    print(res)