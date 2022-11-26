import sys
t = sys.stdin.readline
n = int(t())
res = [False]*201
for _ in range(n):
    a, b = t().split()
    if res[int(a)] :
        res[int(a)].append(b)
    else :
        res[int(a)] = [b]

for idx, i in enumerate(res) :
    if i :
        for j in i :
            print(idx, j)