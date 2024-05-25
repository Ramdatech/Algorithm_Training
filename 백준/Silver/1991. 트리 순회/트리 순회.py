import sys
t = sys.stdin.readline
n = int(t())
dp = {}
for _ in range(n):
    a, b, c = t().strip().split()
    dp[a] = (b, c)
res = ["", "", ""]
def rec(cur, text, num) :
    global pre
    if num == 0 :
        res[num] += cur
    if dp[cur][0] != "." :
        rec(dp[cur][0], text, num)
    if num == 1 :
        res[num] += cur
    if dp[cur][1] != "." :
        rec(dp[cur][1], text, num)
    if num == 2 :
        res[num] += cur

for i in range(3):
    rec("A", "", i)

print(*res, sep="\n")