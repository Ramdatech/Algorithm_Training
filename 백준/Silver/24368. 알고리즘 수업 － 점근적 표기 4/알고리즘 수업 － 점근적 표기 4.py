import sys, math
t = sys.stdin.readline
a, b, c = map(int, t().split())
w = int(t())
n = int(t())


def chk(a, b, c, w, n):
    def g(x):
        return (a - w) * x ** 2 + b * x + c

    na, nb, nc = a - w, b, c

    if na > 0 :
        return 0

    elif na < 0:
        nx = -nb/(2*na)
        ny = g(nx)

        if ny <= 0:
            return 1
        if g(n) <= 0 and nx <= n :
            return 1
        else:
            return 0
    else :
        if nb == 0:
            if nc <= 0:
                return 1
            else:
                return 0
        else:
            root = -nc/nb
            if nb > 0:
                if root >= n:
                    return 1
                else:
                    return 0
            else:
                if root < n:
                    return 1
                else:
                    return 0

        
print(chk(a, b, c, w, n))