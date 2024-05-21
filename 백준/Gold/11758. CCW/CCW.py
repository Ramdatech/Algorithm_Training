import sys
t = sys.stdin.readline
x, y = zip(*[list(map(int, t().split())) for _ in range(3)])
x1, x2, x3 = x
y1, y2, y3 = y
t = x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3
if t != 0 :
    print(t//abs(t))
else :
    print(0)