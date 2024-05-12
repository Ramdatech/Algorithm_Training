import sys, heapq

t = sys.stdin.readline
n = int(t().strip())
arr = []
for _ in range(n) :
    m = int(t().strip())
    if arr and m == 0 :
        print(heapq.heappop(arr))
    elif m == 0 :
        print(0)
    else :
        heapq.heappush(arr, m)