import sys
from collections import deque
t = sys.stdin.readline
M, N, H = map(int, t().split())
ls = [[list(map(int, t().split())) for _ in range(N)] for _ in range(H)]
stt = [(i, j, k) for i in range(H) for j in range(N) for k in range(M) if ls[i][j][k] == 1]
que = deque(stt)
dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
while que:
    z, y, x = que.popleft()
    for dz, dy, dx in dirs:
        nz, ny, nx = z+dz, y+dy, x+dx
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and ls[nz][ny][nx] == 0:
            ls[nz][ny][nx] = ls[z][y][x] + 1
            que.append((nz, ny, nx))

tmp = sum([sum(j,[]) for j in ls],[])
if all(tmp):
    print(max(tmp)-1)
else:
    print(-1)