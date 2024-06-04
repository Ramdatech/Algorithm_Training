import sys
from collections import deque
t = sys.stdin.readline
n, m = map(int, t().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, t().split())
    graph[a].append(b)
    graph[b].append(a)
dp = [[0]*(n+1) for _ in range(n+1)]

def bfs(stt):
    que = deque([stt])
    vst = set([stt])
    dp[stt][stt] = 0
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if nxt in vst or dp[stt][nxt]: continue
            vst.add(nxt)
            dp[stt][nxt] = dp[stt][cur] + 1
            que.append(nxt)

mn = 1e9
res = 0
for i in range(1, n+1):
    bfs(i)
    if mn > sum(dp[i]):
        mn = sum(dp[i])
        res = i
print(res)