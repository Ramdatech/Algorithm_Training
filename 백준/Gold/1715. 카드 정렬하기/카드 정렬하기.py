import sys, heapq
t = sys.stdin.readline
n = int(t())
ls = [int(t()) for x in range(n)]
heapq.heapify(ls)
res = 0
while len(ls) > 1 :
    a, b = heapq.heappop(ls), heapq.heappop(ls)
    res += a+b
    heapq.heappush(ls, a+b)

print(res)