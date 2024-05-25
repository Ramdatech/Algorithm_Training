import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().split())
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
ls = []
for i in range(n):
    tmp = list(t().strip())
    if "I" in tmp :
        pnt = (i, tmp.index("I"))
    ls.append(tmp)
res = 0
que = deque([pnt])
while que :
    x, y = que.popleft()
    for dx, dy in dirs :
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] != "X" :
            que.append((nx, ny))
            if ls[nx][ny] == "P" :
                res += 1
            ls[nx][ny] = "X"


print(res if res != 0 else "TT")