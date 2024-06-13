import sys
t = sys.stdin.readline
h, w = map(int, t().split())
res = [0, 0, 0, 0, 0]
cnt = 0
floor = 0
for _ in range(h) :
    tmp = t().strip()

    flr = 0
    for c in range(4) :
        tmp = t().strip().split("#")[1:-1]
        for n, i in enumerate(tmp) :
            if i == "****" :
                flr += 10**n

    for i in str(flr).zfill(w):
        res[int(i)] += 1

tmp = t().strip()
print(*res)