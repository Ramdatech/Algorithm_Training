import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [list(t().strip()) for x in range(n)]
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
que = deque([(0, 0, 1)])
vst = set()
while que :
    x, y, cnt = que.popleft()
    if (x, y) in vst : continue
    vst.add((x, y))
    if [x, y] == [n-1, m-1] :
        print(cnt)
        break
    for dx, dy in dirs :
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == '1' :
            que.append((nx, ny, cnt+1))