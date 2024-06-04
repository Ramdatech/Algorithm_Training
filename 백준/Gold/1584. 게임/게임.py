import sys, heapq
t = sys.stdin.readline
n = int(t())
danger = [list(map(int, t().split())) for _ in range(n)]
m = int(t())
death = [list(map(int, t().split())) for _ in range(m)]

dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

que = []
heapq.heappush(que, (0, 0, 0))
visit = [[0]*501 for _ in range(501)]
for x1, y1, x2, y2 in death:
    t1, t2 = min(x1, x2), min(y1, y2)
    x1, y1, x2, y2 = t1, t2, max(x1, x2), max(y1, y2)
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            visit[i][j] = 1
visit[0][0] = 1
while que:
    cnt, x, y = heapq.heappop(que)
    if x == 500 and y == 500:
        print(cnt)
        break
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <= nx <= 500 and 0 <= ny <= 500 and not visit[nx][ny]:
            d2 = any([True if (x1<=nx<=x2 or x2<=nx<=x1) and (y1<=ny<=y2 or y2<=ny<=y1) else False for x1, y1, x2, y2 in danger])
            if d2:
                heapq.heappush(que, (cnt+1, nx, ny))
            else:
                heapq.heappush(que, (cnt, nx, ny))
            visit[nx][ny] = 1
else:
    print(-1)