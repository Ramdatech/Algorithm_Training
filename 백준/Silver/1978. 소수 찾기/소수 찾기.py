import sys
import math

def prime(n) :
    li = [True] * (n+1)
    limit = math.ceil(math.sqrt(n))
    t = 0
    while 1 :
        if t < 2 :
            li[t] = False
        else :
            if li[t]:
                for i in [t*x for x in range(2, (n//t) + 1)] :
                    li[i] = False
        t += 1
        if t > limit :
            return li

t = sys.stdin.readline
a = int(t())
li = list(map(int,t().split()))
res = prime(max(li))
score = 0
for i in li :
    if res[i] :
        score += 1
print(score)