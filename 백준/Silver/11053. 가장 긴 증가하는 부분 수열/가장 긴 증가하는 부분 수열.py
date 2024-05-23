import sys
t = sys.stdin.readline
n = int(t())
ls = list(map(int, input().split())) 
dp = [1] * n
for i in range(1, n):
    for j in range(0, i):
        if ls[j] < ls[i]:
            dp[i] = max(dp[i], dp[j] + 1)
res = max(dp)
print(res)