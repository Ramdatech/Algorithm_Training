import sys, heapq
t = sys.stdin.readline
n = int(t().strip())
res = []
for _ in range(n) :
    tmp = int(t().strip())
    if tmp != 0 :
        heapq.heappush(res, (abs(tmp), tmp))
        continue
    if res :
        print(heapq.heappop(res)[1])
    else :
        print(0)