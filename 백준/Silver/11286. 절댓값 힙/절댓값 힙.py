import sys, heapq
t = sys.stdin.readline
n = int(t().strip())
res = []
for _ in range(n) :
    tmp = int(t().strip())
    if tmp != 0 :
        heapq.heappush(res, (abs(tmp), int(tmp/abs(tmp))))
        continue
    if res :
        a = heapq.heappop(res)
        print(a[0] * a[1])
    else :
        print(0)