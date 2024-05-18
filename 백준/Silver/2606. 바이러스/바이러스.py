import sys
from collections import deque, defaultdict
t = sys.stdin.readline
n = int(t().strip())
m = int(t().strip())
graph = defaultdict(list)
for i in range(m) :
    a, b = map(int, t().strip().split())
    graph[a].append(b)
    graph[b].append(a)

que = deque([1])
vst = set()
while que :
    x = que.popleft()
    if x in vst :
        continue
    vst.add(x)

    for t in graph[x] :
        que.append(t)

print(len(vst)-1)
