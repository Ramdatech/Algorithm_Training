import sys, heapq
from collections import deque
t = sys.stdin.readline

def dijk(stt) :
    que = []
    dist = [1e9] * (n**2 + 1)
    heapq.heappush(que, (ls[0][0], stt))
    dist[stt] = ls[0][0]
    while que:
        cost, cur = heapq.heappop(que)
        if dist[cur] < cost:
            continue
        for nxt, ncost in graph[cur]:
            if dist[nxt] > cost + ncost:
                dist[nxt] = cost + ncost
                heapq.heappush(que, (dist[nxt], nxt))
    return dist

for i in range(1, int(1e9)) :
    n = int(t())
    if n == 0 : break

    graph = [[] for _ in range(n**2 + 1)]
    ls = [list(map(int, t().strip().split())) for _ in range(n)]
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    que = deque([(0, 0)])
    vst = set()
    while que:
        x, y = que.popleft()
        if (x, y) in vst: continue
        vst.add((x, y))
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) :
                graph[x * n + y + 1].append((nx * n + ny + 1, ls[nx][ny]))
                que.append((nx, ny))

    mid = dijk(1)
    print(f"Problem {i}:",mid[-1])