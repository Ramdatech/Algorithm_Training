import sys
t = sys.stdin.readline
n = int(t())
P = "I" + "OI"*n
lenS = int(t())
S = t().strip()
res = 0
jump = 1
for i in range(0, lenS-len(P)+1, jump):
    if S[i:i+len(P)] == P :
        res += 1
        jump = 2
    else :
        jump = 1
print(res)