import sys, heapq
t = sys.stdin.readline
n, m, x = map(int, t().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, t().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijk(stt) :
    que = []
    dist = [1e9] * (n + 1)
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

mid = dijk(x)
print(max([dijk(i)[x]+mid[i] for i in range(1, n + 1)]))