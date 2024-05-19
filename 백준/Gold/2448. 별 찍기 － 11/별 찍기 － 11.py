import math
n = int(input())
n = n//3
res = int(math.log2(n))

def recurse(n):
    if n == 0 :
        return [" "*2 + "*" + " "*2, " " + "*" + " " + "*" + " ", "*"*5]

    a = recurse(n-1)

    b = [" "*(3 * 2**(n-1)) + i + " "*(3 * 2**(n-1)) for i in a]
    b += [i + " " + i for i in a]
    return b

print("\n".join(recurse(res)))