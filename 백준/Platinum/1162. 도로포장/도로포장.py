import sys, heapq
t = sys.stdin.readline
n, m, s = map(int, t().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, t().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [[1e12 for _ in range(s+1)] for _ in range(n+1)]

def dijk(stt) :
    que = []
    heapq.heappush(que, (0, 0, stt))
    dist[stt][0] = 0

    while que :
        cost, cut, cur = heapq.heappop(que)
        if dist[cur][cut] < cost :
            continue
        for nxt, nc in graph[cur] :
            if cut < s and dist[nxt][cut+1] > cost :
                dist[nxt][cut+1] = cost
                heapq.heappush(que, (cost, cut+1, nxt))
            if dist[nxt][cut] > cost + nc :
                dist[nxt][cut] = cost + nc
                heapq.heappush(que, (cost+nc, cut, nxt))

dijk(1)
print(min(dist[n]))