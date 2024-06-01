import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
graph = [[] for _ in range(m+1)]
for i in range(m):
    graph[i].append((i+1, 1))
for _ in range(n):
    a, b, c = map(int, t().split())
    if b > m : continue
    graph[a].append((b, c))

def dijk(stt) :
    dist = [1e9]*(m+1)
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

res = dijk(0)
print(res[m])