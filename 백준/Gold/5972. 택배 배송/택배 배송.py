import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, t().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijk(stt) :
    dist = [1e9]*(n+1)
    dist[stt] = 0
    que = []
    heapq.heappush(que, (0, stt))
    while que :
        cost, cur = heapq.heappop(que)
        if dist[cur] < cost : continue
        for nxt, ncost in graph[cur] :
            ncost += cost
            if ncost < dist[nxt] :
                dist[nxt] = ncost
                heapq.heappush(que, (ncost, nxt))
    return dist

res = dijk(1)
print(res[n])