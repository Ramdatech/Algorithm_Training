import sys
t = sys.stdin.readline
n = int(t())
li = list(map(int, t().split()))
se = sorted(list(set(li)))
res = {}

for idx, i in enumerate(se):
    res[i] = idx

for i in li :
     print(res[i], end=" ")