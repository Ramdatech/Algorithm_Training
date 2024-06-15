import sys, math
t = sys.stdin.readline
ls = map(int, t().split())
c0 = int(t())
n0 = int(t())

def chk(lst, w, n):
    def g(x):
        return (a - w) * x ** 2 + nb * x + nc
    a, nb, nc = lst
    na = a - w

    if na > 0 :
        return 0

    if na < 0:
        nx = -nb/(2*na)
        ny = g(nx)
        if ny <= 0 or (g(n) <= 0 and nx <= n):
            return 1
        return 0
    
    if nb == 0:
        if nc <= 0:
            return 1
        return 0
    rt = -nc/nb
    if nb > 0:
        if rt >= n:
            return 1
        return 0
    if rt < n:
        return 1
    return 0

print(chk(ls, c0, n0))