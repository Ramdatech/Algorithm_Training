import sys
t = sys.stdin.readline
n = int(t())
ls = [t().strip() for _ in range(n)]
ls2 = [t().strip() for _ in range(n)]
res = []
for i in ls :
    while ls2 :
        a = ls2.pop(0)
        if i == a :
            break
        elif i in res :
            ls2 = [a] + ls2
            break
        elif i != a:
            res.append(a)
print(len(res))