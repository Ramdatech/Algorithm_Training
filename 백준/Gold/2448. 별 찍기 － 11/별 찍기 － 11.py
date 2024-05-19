import math
n = int(input())
res = int(math.log2(n//3))

def rec(n):
    if n == 0 :
        return [" "*2 + "*" + " "*2, " " + "*" + " " + "*" + " ", "*"*5]

    a = rec(n-1)
    t = 3*2**(n-1)
    b = [" "*t + i + " "*t for i in a]
    b += [i + " " + i for i in a]
    return b

print("\n".join(rec(res)))