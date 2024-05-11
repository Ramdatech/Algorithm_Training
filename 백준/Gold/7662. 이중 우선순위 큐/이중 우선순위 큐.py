import sys, heapq
t = sys.stdin.readline
n = int(t().strip())

def solution(operations):
    mx, mn = [], []
    dels = set([])
    res = []
    for n, i in enumerate(operations) :
        cmd, num = i.split()
        num = int(num)
        if cmd == "I" :
            heapq.heappush(mx, (-num, n))
            heapq.heappush(mn, (num, n))
        elif num == 1 :
            while mx :
                tmp = heapq.heappop(mx)
                if tmp[-1] not in dels :
                    dels.add(tmp[-1])
                    break
        elif num == -1 :
            while mn :
                tmp = heapq.heappop(mn)
                if tmp[-1] not in dels :
                    dels.add(tmp[-1])
                    break
    while mx :
        tmp = heapq.heappop(mx)
        if tmp[-1] not in dels :
            res.append(-tmp[0])
            break
    while mn :
        tmp = heapq.heappop(mn)
        if tmp[-1] not in dels :
            res.append(tmp[0])
            break
    if res == [] :
        print("EMPTY")
    else :
        print(*res)

for _ in range(n) :
    a = int(t().strip())
    ls = [t().strip() for __ in range(a)]
    solution(ls)