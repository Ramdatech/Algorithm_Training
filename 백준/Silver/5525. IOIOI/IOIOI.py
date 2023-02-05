import sys
t = sys.stdin.readline
n = int(t())
P = "I" + "OI"*n
lenS = int(t())
S = t().strip()
res = 0
for i in range(lenS-len(P)+1):
    if S[i:i+len(P)] == P :
        res += 1
print(res)