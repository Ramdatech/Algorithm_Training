import sys
from collections import deque, defaultdict
t = sys.stdin.readline
n = int(t())
s, e = map(int, t().split())
m = int(t())
graph = defaultdict(set)
for _ in range(m) :
    a, b = map(int, t().split())
    graph[a].add(b)
    graph[b].add(a)

def bfs(stt):
    que = deque([(stt, 0)])
    vst = set()
    while que:
        x, cnt = que.popleft()
        if x in vst: continue
        if x == e: break
        vst.add(x)
        for dx in graph[x]:
            if dx not in vst:
                que.append((dx, cnt+1))
    else :
        return -1
    return cnt

print(bfs(s))