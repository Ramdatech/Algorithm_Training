import sys
from collections import deque
t = sys.stdin.readline
n = int(t())
ls = [list(t().strip()) for x in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(stt, target, ls):
    que = deque([stt])
    vst = set()
    while que:
        x, y = que.popleft()
        if (x, y) in vst: continue
        vst.add((x, y))
        ls[x][y] = '0'
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and ls[nx][ny] in list(target):
                que.append((nx, ny))
    return len(vst)

res = [0, 0]
for i in range(n):
    for j in range(n):
        if ls[i][j] == 'B':
            res[0] += 1
            res[1] += 1
            bfs((i, j), 'B', ls)

ls2 = [list(x) for x in ls]

for i in range(n):
    for j in range(n):
        if ls[i][j] == 'G':
            res[0] += 1
            bfs((i, j), 'G', ls)
        if ls[i][j] == 'R':
            res[0] += 1
            bfs((i, j), 'R', ls)

for i in range(n):
    for j in range(n):
        if ls2[i][j] == 'G' or ls2[i][j] == 'R':
            res[1] += 1
            bfs((i, j), 'RG', ls2)

print(*res)
