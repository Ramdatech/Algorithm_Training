import sys, heapq
from collections import deque
t = sys.stdin.readline
n = int(t())
m = int(t())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, t().split())
    graph[a].append((b, c))

x, y = map(int, t().split())

def dijk(stt) :
    que = []
    dist = [1e9] * (n + 1)
    heapq.heappush(que, (0, stt, [stt]))
    dist[stt] = 0
    load = [[]] * (n+1)
    while que:
        cost, cur, hist = heapq.heappop(que)
        if dist[cur] < cost:
            continue
        load[cur] = hist
        for nxt, ncost in graph[cur]:
            if dist[nxt] > cost + ncost:
                dist[nxt] = cost + ncost
                load[nxt] = hist + [nxt]
                heapq.heappush(que, (dist[nxt], nxt, hist + [nxt]))
    return dist, load

res, load = dijk(x)
print(res[y])
print(len(load[y]))
print(*load[y])