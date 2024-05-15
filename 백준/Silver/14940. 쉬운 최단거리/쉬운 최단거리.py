import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().strip().split())
ls = []
stt = []
for i in range(n) :
    tmp = list(map(int, t().strip().replace("1", "-1").split()))
    ls.append(tmp)
    if stt == [] and 2 in tmp:
        stt.append((i, tmp.index(2), 0))
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
        if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == -1 :
            que.append((nx, ny, cnt+1))

for i in ls :
    print(*i)