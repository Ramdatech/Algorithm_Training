import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().split())
dirs = [(0,1), (0,-1), (1,0), (-1,0)]
ls = []
chz = set()
for i in range(n):
    tmp = [x+1 for x in list(map(int, t().split()))]
    ls.append(tmp)
    chz.update([(i, x) for x in range(m) if tmp[x] == 2])

vst = set()
def bfs(stt) :
    que = deque([stt])
    while que :
        x,y = que.popleft()
        if (x,y) in vst : continue
        vst.add((x,y))
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 1:
                ls[nx][ny] = 0
                que.append((nx, ny))
bfs((0,0))

res = 0
while chz :
    tmp = set()
    for x,y in chz:
        s = sum([1 for dx, dy in dirs if 0 <= x+dx < n and 0 <= y+dy < m and ls[x+dx][y+dy] == 0])
        if s >= 2:
            tmp.add((x,y))
    res += 1
    for x,y in tmp:
        ls[x][y] = 0
        bfs((x,y))
    chz = chz - tmp
print(res)