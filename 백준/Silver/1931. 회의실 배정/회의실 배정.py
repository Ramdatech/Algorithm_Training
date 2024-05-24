import sys, heapq
t = sys.stdin.readline
n = int(t())
ls = []
for _ in range(n):
    a, b = map(int, t().split())
    heapq.heappush(ls, (b, a))
tmp, res = 0, 0
for _ in range(n) :
    b, a = heapq.heappop(ls)
    if a >= tmp :
        tmp = b
        res += 1
print(res)