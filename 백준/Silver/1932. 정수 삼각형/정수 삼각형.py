import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, t().strip().split())) for _ in range(n)]
for i in range(1, n) :
    for j in range(i+1) :
        if j == 0 :
            ls[i][j] += ls[i-1][j]
        elif j == i :
            ls[i][j] += ls[i-1][j-1]
        else :
            ls[i][j] += max(ls[i-1][j-1], ls[i-1][j])
print(max(ls[n-1]))