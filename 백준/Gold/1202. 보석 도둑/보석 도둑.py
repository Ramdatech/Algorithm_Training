import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
ls = sorted([list(map(int, t().split())) for _ in range(n)])
bg = sorted([int(t()) for _ in range(m)])
que, res, idx = [], 0, 0
for i in range(m):
    while idx < n and ls[idx][0] <= bg[i]:
        heapq.heappush(que, -ls[idx][1])
        idx += 1
    if que:
        res -= heapq.heappop(que)
print(res)