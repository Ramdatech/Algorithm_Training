import sys
t = sys.stdin.readline
n = int(t())
dp = {}
for _ in range(n):
    a, *b = t().strip().split()
    dp[a] = b
res = [""]*3
def r(n, t):
    res[n] += t
def rec(cur) :
    r(0, cur)
    o, p = [x!="." for x in dp[cur]]
    if o : rec(dp[cur][0])
    r(1, cur)
    if p : rec(dp[cur][1])
    r(2, cur)
rec("A")
print(*res, sep="\n")