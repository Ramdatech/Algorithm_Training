import sys
from collections import defaultdict, deque

t = sys.stdin.readline
n, m = map(int, t().strip().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, t().strip().split())
    graph[a].append(b)
    graph[b].append(a)

vst = [False] * (n+1)

def bfs(stt):
    que = deque([stt])
    while que :
        x = que.popleft()
        if vst[x] : continue
        vst[x] = True
        for nx in graph[x]:
            if not vst[nx]:
                que.append(nx)

res = 0
for i in range(1, n+1):
    if not vst[i]:
        bfs(i)
        res += 1

print(res)