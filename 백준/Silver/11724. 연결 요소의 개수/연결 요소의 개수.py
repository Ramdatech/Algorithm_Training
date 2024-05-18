import sys
from collections import defaultdict, deque

t = sys.stdin.readline
n, m = map(int, t().strip().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, t().strip().split())
    graph[a].append(b)
    graph[b].append(a)

vst = set()

def bfs(stt):
    que = deque([stt])
    while que :
        x = que.popleft()
        if x in vst :
            continue
        vst.add(x)
        for nx in graph[x]:
            que.append(nx)

res = 0
for i in range(1, n+1):
    if i not in vst :
        bfs(i)
        res += 1

print(res)