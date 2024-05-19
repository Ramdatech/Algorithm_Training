n = int(input())
n = n//3
res = 0
while n % 2 == 0:
    n = n//2
    res += 1

def recurse(n):
    if n == 0 :
        a = []
        a += [" "*2 + "*" + " "*2]
        a += [" " + "*" + " " + "*" + " "]
        a += ["*"*5]
        return a

    a = recurse(n-1)

    b = []
    for i in a:
        b.append(" "*(3 * 2**(n-1)) + i + " "*(3 * 2**(n-1)))
    for i in a:
        b.append(i + " " + i)
    return b


print("\n".join(recurse(res)))