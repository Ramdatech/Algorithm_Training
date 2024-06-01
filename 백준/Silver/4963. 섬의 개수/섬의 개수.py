import sys
from collections import deque
t = sys.stdin.readline
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def bfs(x, y) :
    que = deque([(x, y)])
    vst = set((x, y))
    while que :
        x, y = que.popleft()
        for dx, dy in dirs :
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 1 and (nx, ny) not in vst :
                que.append((nx, ny))
                vst.add((nx, ny))
                ls[nx][ny] = 0

while 1 :
    m, n = map(int, t().split())
    if m == 0 and n == 0 : break
    ls = [list(map(int, t().split())) for _ in range(n)]

    res = 0
    for i in range(n) :
        for j in range(m) :
            if ls[i][j] == 1 :
                bfs(i, j)
                res += 1
    print(res)