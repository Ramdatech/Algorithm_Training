import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().split())
ls, shk = [], []
for i in range(n):
    tmp = list(map(int, t().strip().split()))
    for j in range(m):
        if tmp[j] == 1:
            shk.append((i, j))
    ls.append(tmp)

dist = [[1e9]*m for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
def bfs(x, y):
    q = deque([(x, y)])
    dist[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and dist[x][y]+1 < dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

for x, y in shk:
    bfs(x, y)

print(max(sum(dist, [])))