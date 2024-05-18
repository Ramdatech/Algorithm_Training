import sys
t = sys.stdin.readline
a, b, c, d, e, f = map(int, t().strip().split())
print((c*e-f*b)//(a*e-b*d), (c*d-f*a)//(b*d-a*e))