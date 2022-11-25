import sys
import math
def prime(n) :
    li = [True]*(n+1)
    limit = math.ceil(math.sqrt(n))
    for t in range(len(li)) :
        if t < 2 :
            li[t] = False
        else :
            if li[t]:
                for i in [t*x for x in range(2, n//t+1)] :
                    li[i] = False
        if t >= limit :
            return li

m = prime(10000)
t = sys.stdin.readline
n = int(t())
for _ in range(n):
    a = int(t())
    res = [0, a]
    for i in range(a//2, -1, -1) :
        if m[i]+m[a-i] == 2 :
            res = [i, a-i]
            break
    print(f'{res[0]} {res[1]}')