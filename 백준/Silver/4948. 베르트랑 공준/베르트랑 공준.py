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

m = prime(123456*2)
while 1 :
    a = int(sys.stdin.readline())
    if a==0:
        break
    print(sum(m[a+1:2*a+1]))