import sys, heapq
from collections import deque
t = sys.stdin.readline
n = int(t())

def dijk(stt):
    que = []
    dist = [1e9] * (m + 1)
    heapq.heappush(que, (0, stt))
    dist[stt] = 0
    while que:
        cost, cur = heapq.heappop(que)
        for nxt, ncost in graph[cur]:
            if dist[nxt] > cost + ncost:
                dist[nxt] = cost + ncost
                heapq.heappush(que, (dist[nxt], nxt))
    return dist

for _ in range(n):
    m, d, co = map(int, t().split())

    graph = [[] for _ in range(m + 1)]
    for _ in range(d):
        a, b, c = map(int, t().split())
        graph[b].append((a, c))

    res = [x for x in dijk(co) if x < 1e9]
    print(len(res), max(res))