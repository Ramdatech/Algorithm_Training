import sys, bisect
t = sys.stdin.readline
n = int(t())
ls = sorted(list(map(int, t().strip().split())))
res = 0

for idx, goal in enumerate(ls):
    tmplist = ls[:idx] + ls[idx+1:]
    for j in range(n-1):
        a, b = sorted([goal-ls[j], ls[j]])
        if idx == j : continue
        p1 = bisect.bisect_left(tmplist, a, 0, n-1)
        p2 = bisect.bisect_right(tmplist, b, 0, n-1)-1
        if p1 != p2 and tmplist[p1] == a and tmplist[p2] == b :
            res += 1
            break
print(res)