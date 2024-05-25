import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, t().strip().split())) for _ in range(n)]
vst = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
vst[0][1] = [1, 0, 0]
for i in range(1, 2*n-1) :
    for x, y in [(j, i-j) for j in range(i+1) if 0<=j<n and 0<=i-j<n] :
        if ls[x][y] == 1 :
            continue
        if 0<=x < n and 0<=y-1 < n and ls[x][y-1] == 0 :
            vst[x][y][0] += vst[x][y-1][2] + vst[x][y-1][0]
        if 0<=x-1 < n and 0<=y < n and ls[x-1][y] == 0 :
            vst[x][y][1] += vst[x-1][y][1] + vst[x-1][y][2]
        if 0<=x-1 < n and 0<=y-1 < n and ls[x-1][y-1] == 0 and ls[x-1][y] == 0 and ls[x][y-1] == 0 :
            vst[x][y][2] += sum(vst[x-1][y-1])
print(sum(vst[-1][-1]))