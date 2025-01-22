import heapq

n = int(input())
m = int(input())
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

for i in range(m):
    a, b, c = map(int, input().split())
    if a == b : continue
    heapq.heappush(msk, (c, a, b))

result = 0
while msk :
    scr, p1, p2 = heapq.heappop(msk)
    if find_prt(p1) != find_prt(p2):
        union_find(p1, p2)
        result += scr

print(result)