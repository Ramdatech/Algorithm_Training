import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
msk = list(map(int, t().strip().split()))
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, t().split())
    if msk[a] == 0 and msk[b] == 0 or n-1 in (a, b):
        graph[a].append((b, c))
        graph[b].append((a, c))

que = []
heapq.heappush(que, (0, 0))
dist = [1e15] * (n+1)
dist[0] = 0
while que:
    d, cur = heapq.heappop(que)
    if cur == n-1 :
        print(d)
        break
    if dist[cur] < d:
        continue
    for nxt, cost in graph[cur] :
        if dist[nxt] > d + cost:
            dist[nxt] = d + cost
            heapq.heappush(que, (dist[nxt], nxt))
else :
    print(-1)