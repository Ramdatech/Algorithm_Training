import sys, heapq
t = sys.stdin.readline
n = int(t())
if n == 0 :
    print(0)
elif n < 3 :
    ls = [int(t()) for _ in range(n)]
    print(sum(ls))
else :
    ls = [0] + [int(t()) for _ in range(n)]
    dp = [0] * (n+1)
    dp[0] = ls[0]
    dp[1] = ls[0] + ls[1]
    dp[2] = max(ls[0] + ls[2], ls[1] + ls[2])
    for i in range(3, n+1) :
        dp[i] = max(ls[i]+dp[i-2], ls[i]+ls[i-1]+dp[i-3])
    print(dp[-1])