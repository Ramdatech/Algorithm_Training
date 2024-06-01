import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, t().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

p1, p2 = map(int, t().split())

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

start = dijk(1)
mid = dijk(p1)[p2]
end = dijk(n)
res = min(start[p1] + mid + end[p2], start[p2] + mid + end[p1])
print(res if res < 1e9 else -1)