import sys
t = sys.stdin.readline
K, N = t().strip().split()
res = 0 
for n, v in enumerate(list(str(K))) : 
    if v.isdecimal() :
        tmp = int(v)
    else : 
        tmp = int(ord(v)-55)
    tmp *= (int(N)**((len(K)-1)-n))
    res += tmp

print(res)

           