import sys
from collections import deque
t = sys.stdin.readline
n = int(t())
n, s, m = map(int, t().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c, d = map(int, t().split())
    graph[a].append((b, c, d))

dist = [[1e12 for _ in range(s+1)] for _ in range(n+1)]
dist[1][0] = 0

for i in range(s+1):
    for j in range(1, n+1):
        if dist[j][i] == 1e12:
            continue
        for nxt, ntic, ncost in graph[j]:
            if i + ntic <= s and dist[nxt][i+ntic] > dist[j][i] + ncost:
                dist[nxt][i+ntic] = dist[j][i] + ncost

if min(dist[-1]) == 1e12 :
    print("Poor KCM")
else :
    print(min(dist[-1]))