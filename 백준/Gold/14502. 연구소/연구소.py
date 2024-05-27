import sys
from collections import deque
from itertools import combinations
t = sys.stdin.readline
n, m = map(int, t().strip().split())
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
stt, fld, ls = [], [], []
for i in range(n) :
    tmp = list(map(int, t().strip().split()))
    for j in range(m) :
        if tmp[j] == 2 :
            stt.append((i, j))
        elif tmp[j] == 0 :
            fld.append((i, j))
    ls.append(tmp)

def bfs(stt, ban):
    que = deque(stt)
    vst = set()
    tmp = 0
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and ls[nx][ny] == 0 and (nx, ny) not in vst and (nx, ny) not in ban:
                que.append((nx, ny))
                vst.add((nx, ny))
    return len(vst)

res = 0
for ban in combinations(fld, 3):
    res = max(res, len(fld)-bfs(stt, ban)-3)
print(res)