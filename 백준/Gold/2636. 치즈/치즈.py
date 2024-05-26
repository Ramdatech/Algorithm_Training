import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().strip().split())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
stt, ls = [], []
vst = set()
for i in range(n) :
    tmp = list(map(int, t().strip().split()))
    for j in range(m) :
        if tmp[j] == 1 :
            stt.append((i, j))
        tmp[j] += 1
    ls.append(tmp)

def bfs(stt):
    que = deque(stt)
    while que:
        x, y = que.popleft()
        if (x, y) in vst: continue
        vst.add((x, y))
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 1 :
                que.append((nx, ny))
                ls[nx][ny] = 0

bfs([(0, 0)])
res, prev = 0, 0

while 1 :
    tmp_stt = []
    for x, y in stt :
        if ls[x][y] == 0 : continue
        tmp = sum([1 for dx, dy in dirs if 0 <= x+dx < n and 0 <= y+dy < m and ls[x+dx][y+dy] == 0])
        if tmp >= 1 :
            tmp_stt.append((x, y))

    for x, y in tmp_stt :
        ls[x][y] = 0
    if tmp_stt == [] :
        break
    prev = len(tmp_stt)
    res += 1
    bfs(tmp_stt)
print(res)
print(prev)