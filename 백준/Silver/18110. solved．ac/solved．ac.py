import sys
t = sys.stdin.readline
n = int(t().strip())
if n == 0 :
    print(0)
else : 
    tmp = (15*n)//100
    tmp += 0 if (15*n)/100 - (15*n)//100 < 0.5 else 1
    ls = sorted([int(t().strip()) for _ in range(n)])
    ls = ls[tmp : n-tmp]
    res = sum(ls)//len(ls)
    res += 0 if sum(ls)/len(ls) - sum(ls)//len(ls) < 0.5 else 1
    print(res)
