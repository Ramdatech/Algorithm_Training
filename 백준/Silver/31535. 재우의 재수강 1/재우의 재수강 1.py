import heapq
ex, ey = map(int, input().split())
n, gy = map(int, input().split())
ls = zip(*[list(map(int, input().split()))[::-1] for _ in range(2)])
msk = [0]*ey
for a, b in ls :
    for j in range(a):
        msk[j] = b
msk.append(msk[-1])

que = [[0,0,0]]
vst = {}
mx = 1e9
while que :
    t, x, y = heapq.heappop(que)
    if (x,y) == (ex, gy) and t < mx:
        mx = t
    if (x,y) in vst and vst[(x,y)] < t : continue
    vst[(x,y)] = t
    for dx, dy in [(0,1),(0,-1),(1,0)] :
        nx, ny = x+dx, y+dy
        if 0<=nx<=ex and 0<=ny<=ey and ((nx,ny) not in vst or t+msk[y] < vst[(nx,ny)]):
            vst[(nx,ny)] = t+msk[min(y, ny)]
            heapq.heappush(que, [t+msk[min(y, ny)], nx, ny])
print(mx)