import sys
from collections import deque
t = sys.stdin.readline
n = int(t())
ls = [list(t().strip()) for x in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(stt):
    que = deque([stt])
    vst = set()
    while que:
        x, y = que.popleft()
        if (x, y) in vst: continue
        vst.add((x, y))
        ls[x][y] = '0'
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and ls[nx][ny] == '1':
                que.append((nx, ny))
    return len(vst)

res = []
for i in range(n):
    for j in range(n):
        if ls[i][j] == '1':
            res.append(bfs((i, j)))

print(len(res))
print(*sorted(res), sep='\n')