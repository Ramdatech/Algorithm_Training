import sys
x1,y1,x2,y2,x3,y3 = map(int, sys.stdin.buffer.read().split())
t = x1*y2+x2*y3+x3*y1-x2*y1-x3*y2-x1*y3
if t != 0 :
    print(t//abs(t))
else :
    print(0)