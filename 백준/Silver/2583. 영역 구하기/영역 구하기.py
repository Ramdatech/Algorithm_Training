import sys
from collections import deque
t = sys.stdin.readline
n, m, s = map(int, t().split())
ls = [[0]*m for _ in range(n)]
for _ in range(s):
    x, y, w, h = map(int, t().split())
    for i in range(x, w):
        for j in range(y, h):
            ls[j][i] = 1

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(stt):
    que = deque([stt])
    vst = set()
    while que:
        x, y = que.popleft()
        if (x, y) in vst: continue
        vst.add((x, y))
        ls[x][y] = 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 0:
                que.append((nx, ny))
    return len(vst)

res = []
for i in range(n):
    for j in range(m):
        if ls[i][j] == 0:
            res.append(bfs((i, j)))

print(len(res))
print(*sorted(res))