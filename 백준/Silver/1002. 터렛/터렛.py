import sys
import math
input = sys.stdin.readline
n = int(input().strip())
for i in range(n) :
    x1, y1, r1, x2, y2, r2 = map(int,sys.stdin.readline().strip().split())
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    distance = math.sqrt(dx**2 + dy**2)
    if abs(r1-r2) < distance < abs(r1+r2):
        print(2)
    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif abs(r1+r2) == distance or abs(r1-r2) == distance :
        print(1)
    else :
        print(0)