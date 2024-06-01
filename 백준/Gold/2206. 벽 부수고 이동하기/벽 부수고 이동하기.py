import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().strip().split())
ls = [list(map(int, list(t().strip()))) for _ in range(n)]
dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
msk = [[[False, False] for _ in range(m)] for _ in range(n)]

que = deque([(0, 0, 0, 1)])
msk[0][0][0] = True

while que :
    x, y, b, dist = que.popleft()
    if x == n - 1 and y == m - 1:
        print(dist)
        sys.exit(0)

    for dx, dy in dirs :
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m :
            if ls[nx][ny] == 0 and not msk[nx][ny][b] :
                msk[nx][ny][b] = True
                que.append((nx, ny, b, dist+1))
            elif b == 0 and not msk[nx][ny][b] :
                msk[nx][ny][1] = True
                que.append((nx, ny, 1, dist+1))

print(-1)