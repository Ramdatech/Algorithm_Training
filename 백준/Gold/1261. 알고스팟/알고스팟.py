import sys, heapq
from collections import deque
t = sys.stdin.readline
m, n = map(int, t().split())
graph = [[] for _ in range(n * m + 1)]
ls = [list(map(int, list(t().strip()))) for _ in range(n)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
que = deque([(0, 0)])
vst = set()
while que:
    x, y = que.popleft()
    if (x, y) in vst: continue
    vst.add((x, y))
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and (nx, ny) :
            graph[x * m + y + 1].append((nx * m + ny + 1, ls[nx][ny]))
            que.append((nx, ny))

def dijk(stt) :
    que = []
    dist = [1e9] * (n * m + 1)
    heapq.heappush(que, (0, stt))
    dist[stt] = 0
    while que:
        cost, cur = heapq.heappop(que)
        if dist[cur] < cost:
            continue
        for nxt, ncost in graph[cur]:
            if dist[nxt] > cost + ncost:
                dist[nxt] = cost + ncost
                heapq.heappush(que, (dist[nxt], nxt))
    return dist

mid = dijk(1)
print(mid[-1])