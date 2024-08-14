import sys
t = sys.stdin.readline
n, msk = int(t()), 'aeiou'
def f(ls, ls2) :
    (a1, *X, a3), (b1, *Y, b3) = ls, ls2
    if a1 == b1 and a3 == b3 and sorted(X) == sorted(Y) :
        X, Y = [[s for s in L if s not in msk] for L in [X, Y]]
        if X == Y : return "YES"
    return "NO"
print(f(t().strip(), t().strip()))