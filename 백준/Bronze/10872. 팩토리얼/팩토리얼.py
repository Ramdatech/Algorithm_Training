def fac(n, res=1):
    if n <= 1 :
        return res
    res = fac(n-1, res*(n))
    return res

import sys
t = int(sys.stdin.readline().strip())
print(fac(t))