import sys, heapq
t = sys.stdin.readline
n, k = map(int, t().split())
ls = [list(map(int, t().split())) for _ in range(n)]
dp = [0] * (k+1)
for i in range(n):
    for j in range(k, ls[i][0]-1, -1):
        if ls[i][0] <= j:
            dp[j] = max(dp[j], dp[j-ls[i][0]] + ls[i][1])
print(dp[k])
