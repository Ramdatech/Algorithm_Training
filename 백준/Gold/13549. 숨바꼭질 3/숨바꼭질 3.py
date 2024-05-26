import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
dist = [1e9] * 200001

def bfs(stt) :
    que = []
    heapq.heappush(que, (0, stt))
    while que :
        cnt, x = heapq.heappop(que)
        if dist[x] <= cnt :
            continue
        dist[x] = cnt
        if x*2 <= m*2 :
            heapq.heappush(que, (cnt, x * 2))
        if x+1 <= 100000 and x+1 <= m :
            heapq.heappush(que, (cnt+1, x+1))
        if x-1 >= 0 :
            heapq.heappush(que, (cnt+1, x-1))
    return dist[m]
print(bfs(n))