import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [list(t().strip()) for _ in range(n)]
n, m = n+1, m+1
f_ls = [[] for _ in range(n*m)]
r_ls = [[] for _ in range(n*m)]
for i in range(n-1):
    for j in range(m-1):
        a, b, c, d = i*m+j, (i+1)*m+j+1, i*m+j+1, (i+1)*m+j
        if ls[i][j] == '\\':
            if a < n*m and b < n*m:
                f_ls[a].append((b, 1))
                f_ls[b].append((a, 1))
            if c < n*m and d < n*m:
                r_ls[c].append((d, 1))
                r_ls[d].append((c, 1))
        else :
            if c < n*m and d < n*m:
                f_ls[c].append((d, 1))
                f_ls[d].append((c, 1))
            if a < n*m and b < n*m:
                r_ls[a].append((b, 1))
                r_ls[b].append((a, 1))

que = []
heapq.heappush(que, (0, 0, 0))
dist = [(1e9, 1e9)]*(n*m)
dist[0] = (0, 0)
while que :
    cnt, cost, cur = heapq.heappop(que)
    if cur == n*m-1:
        print(cnt)
        break
    
    for nxt, ncost in f_ls[cur]:
        cn, co = dist[nxt]
        if cn > cnt:
            dist[nxt] = (cnt, cost+ncost)
            heapq.heappush(que, (cnt, cost+ncost, nxt))
    for nxt, ncost in r_ls[cur]:
        cn, co = dist[nxt]
        if cn > cnt+1:
            dist[nxt] = (cnt+1, cost+ncost)
            heapq.heappush(que, (cnt+1, cost+ncost, nxt))
else :
    print("NO SOLUTION")