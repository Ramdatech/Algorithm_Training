import sys
from collections import deque

def bfs(key):
    que = deque([key])
    vst = set()

    while que:
        x, y = que.popleft()
        if (x,y) in vst :
            continue
        vst.add((x,y))
        for dx, dy in dirs :
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) in dp :
                que.append((nx, ny))
                dp[(nx, ny)] = 0


t = sys.stdin.readline
cnt = int(t().strip())

for _ in range(cnt) :
    n, m, p = map(int, t().strip().split())
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dp = {}
    for _ in range(p) :
        a, b = map(int, t().strip().split())
        dp[(a, b)] = 1

    res = 0
    for key in dp :
        if dp[key] == 1 :
            bfs(key)
            res += 1
    print(res)