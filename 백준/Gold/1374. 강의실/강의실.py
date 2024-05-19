import sys, heapq
t = sys.stdin.readline
n = int(t().strip())
a = [list(map(int, t().strip().split())) for _ in range(n)]
a.sort(key=lambda x: x[1])
que = []
heapq.heappush(que, a[0][2])
for i in range(1, n):
    if que[0] <= a[i][1]:
        heapq.heappop(que)
    heapq.heappush(que, a[i][2])
print(len(que))