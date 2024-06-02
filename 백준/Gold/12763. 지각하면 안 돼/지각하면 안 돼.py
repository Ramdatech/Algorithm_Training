import sys, heapq
t = sys.stdin.readline
n = int(t())
T, M = map(int, t().split())
L = int(t())
graph = [[] for _ in range(n+1)]
for _ in range(L) :
    a, b, c, d = map(int, t().split())
    graph[a].append((b, c, d))
    graph[b].append((a, c, d))

def dijk(stt):
    dist = []
    que = []
    heapq.heappush(que, (0, 0, stt))
    while que :
        cost, time, cur = heapq.heappop(que)
        if cur == n :
            dist.append(cost)
        for nxt, n_time, n_cost in graph[cur] :
            if time + n_time <= T and cost + n_cost <= M:
                heapq.heappush(que, (cost + n_cost, time + n_time, nxt))

    return dist

res = dijk(1)
print(min(res) if res else -1)