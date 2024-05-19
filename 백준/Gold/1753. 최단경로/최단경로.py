import sys, heapq
from collections import defaultdict
t = sys.stdin.readline
n, m = map(int, t().strip().split())
stt = int(t().strip())
graph = defaultdict(list)
for _ in range(m) :
    a, b, c = map(int, t().strip().split())
    graph[a].append((b, c))

que = []
heapq.heappush(que, (0, stt))
dist = [1e12] * (n+1)
while que :
    dis, x = heapq.heappop(que)
    if dist[x] < dis :
        continue
    dist[x] = dis

    for nx, nd in graph[x] :
        n_cost = dis + nd
        if dist[nx] > n_cost:
            dist[nx] = n_cost
            heapq.heappush(que, (n_cost, nx))

for i in dist[1:] :
    print(i if i != 1e12 else "INF")