import sys
t = sys.stdin.readline
n = int(t())
for _ in range(n):
    m = int(t())
    ls = [list(map(int, t().strip().split())) for _ in range(2)]
    msk = [[0]*m for _ in range(2)]
    msk[0][0] = ls[0][0]
    msk[1][0] = ls[1][0]
    for i in range(1, m):
        tmp = [msk[z][i-j] for z in range(2) for j in range(2, 4) if 0 <= i-j < i-1]
        msk[0][i] = max([msk[1][i-1]] + tmp) + ls[0][i]
        msk[1][i] = max([msk[0][i-1]] + tmp) + ls[1][i]
    print(max(msk[0][-1], msk[1][-1]))