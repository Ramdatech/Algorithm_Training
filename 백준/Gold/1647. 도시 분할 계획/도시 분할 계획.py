import sys
t = sys.stdin.readline
n, m = map(int, t().split())

msk = []
prt = [x for x in range(n+1)]

def find_prt(x):
    if prt[x] != x :
        prt[x] = find_prt(prt[x])
    return prt[x]

def union_find(x, y):
    r1 = find_prt(x)
    r2 = find_prt(y)
    if r1 < r2 :
        prt[r2] = r1
    else :
        prt[r1] = r2

for _ in range(m):
    a, b, c = map(int, t().split())
    if a == b : continue
    elif a < b :
        msk.append((c, a, b))
    else :
        msk.append((c, b, a))

msk.sort()
total_result = 0
max_result = 0
for scr, p1, p2 in msk :
    if find_prt(p1) != find_prt(p2):
        union_find(p1, p2)
        total_result += scr
        max_result = max(max_result, scr)

print(total_result-max_result)