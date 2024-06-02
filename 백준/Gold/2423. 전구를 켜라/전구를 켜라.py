import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [list(t().strip()) for _ in range(n)]
n, m = n+1, m+1
msk = [[[] for _ in range(n*m)] for _ in range(2)]
for i in range(n-1):
    for j in range(m-1):
        a, b, c, d = i*m+j, (i+1)*m+j+1, i*m+j+1, (i+1)*m+j
        addr = 0 if ls[i][j] == '\\' else 1
        if a < n*m and b < n*m:
            msk[addr][a].append(b)
            msk[addr][b].append(a)
        if c < n*m and d < n*m:
            msk[addr^1][c].append(d)
            msk[addr^1][d].append(c)

que = []
heapq.heappush(que, (0, 0))
dist = [0] + [1e9]*(n*m-1)
while que :
    cnt, cur = heapq.heappop(que)
    cur *= -1
    if cur == n*m-1:
        print(cnt)
        break

    for tmp in range(2) :
        for nxt in msk[tmp][cur]:
            if dist[nxt] > cnt + tmp:
                dist[nxt] = cnt + tmp
                heapq.heappush(que, (cnt+tmp, -nxt))
else :
    print("NO SOLUTION")