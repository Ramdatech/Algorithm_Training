import sys, heapq
t = sys.stdin.readline
n = int(t())
m = int(t())
graph = [set() for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, t().split())
    graph[a].add((b, c))

stt, end = map(int, t().split())
que = []
heapq.heappush(que, (0, stt))
dist = [1e12]*(n+1)

while que :
    cost, cur = heapq.heappop(que)
    if dist[cur] < cost : continue
    dist[cur] = cost
    for nx, nc in graph[cur]:
        nnc = cost + nc
        if dist[nx] > nnc:
            dist[nx] = nnc
            heapq.heappush(que, (nnc, nx))
print(dist[end])