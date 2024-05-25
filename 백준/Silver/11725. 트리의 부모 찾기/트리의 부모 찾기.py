import sys
from collections import deque, defaultdict
t = sys.stdin.readline
n = int(t())
graph = defaultdict(set)
for _ in range(n-1):
    a, b = map(int, t().split())
    graph[a].add(b)
    graph[b].add(a)

glob = {}
que = deque([1])
vst = set()
while que:
    cur = que.popleft()
    if cur in vst : continue
    vst.add(cur)
    if cur >= 2 :
        glob[cur] = graph[cur] & vst
    for i in graph[cur]:
        if i not in vst:
            que.append(i)

for i in range(2, n+1):
    print(*glob[i])