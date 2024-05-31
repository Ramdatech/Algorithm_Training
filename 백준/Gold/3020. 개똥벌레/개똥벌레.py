import sys, bisect
t = sys.stdin.readline
n, m = map(int, t().strip().split())
pre, pst = [], []
for i in range(n) :
    a = int(t())
    tmp = pre if i % 2 == 0 else pst
    tmp.append(a)
pre.sort()
pst.sort()

res = [1e12, 0]
for i in range(m) :
    tmp = n-bisect.bisect_left(pre, i+1)-bisect.bisect_left(pst, m-i)
    if tmp < res[0] :
        res = [tmp, 1]
    elif tmp == res[0] :
        res = [tmp, res[1]+1]

print(*res)