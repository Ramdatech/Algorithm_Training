import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().strip().split())
ls = [list(map(int, t().strip().split())) for _ in range(n)]
stt = [(x, y, 0) for x in range(n) for y in range(m) if ls[x][y] == 2]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

que = deque(stt)
vst = set()
while que :
    x, y, cnt = que.popleft()
    if (x, y) in vst : continue
    ls[x][y] = cnt
    vst.add((x, y))

    for dx, dy in dirs :
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 1 :
            que.append((nx, ny, cnt+1))

for i in range(n) :
    for j in range(m) :
        if (i, j) not in vst and ls[i][j] == 1 :
            ls[i][j] = -1

for i in ls :
    print(*i)
