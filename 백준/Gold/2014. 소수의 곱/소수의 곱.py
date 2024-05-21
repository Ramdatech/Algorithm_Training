import sys, heapq
t = sys.stdin.readline
k, n = map(int, t().split())
a = list(map(int, t().strip().split()))
heap = []
for i in a:
    heapq.heappush(heap, i)

while n:
    x = heapq.heappop(heap)
    for i in a:
        heapq.heappush(heap, x*i)
        if x % i == 0:
            break
    n -= 1
print(x)