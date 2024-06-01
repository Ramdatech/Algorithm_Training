import sys
from collections import deque
t = sys.stdin.readline
n = int(t())
knt = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

for _ in range(n) :
    m = int(t())
    msk = [[1e9] * m for _ in range(m)]
    x1, y1 = map(int, t().split())
    x2, y2 = map(int, t().split())

    que = deque([(x1, y1)])
    msk[x1][y1] = 0
    
    while que :
        x, y = que.popleft()
        if x == x2 and y == y2 :
            print(msk[x][y])
            break
        for dx, dy in knt :
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < m and msk[nx][ny] == 1e9 :
                msk[nx][ny] = msk[x][y] + 1
                que.append((nx, ny))