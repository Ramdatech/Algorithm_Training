import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n) :
    res = 0
    x1, y1, x2, y2 = map(int, input().split())
    m = int(input())
    for _ in range(m) :
        a, b, r = map(int, input().split())
        condition_1 = (x1-a)**2 + (y1-b)**2 < r**2
        condition_2 = (x2-a)**2 + (y2-b)**2 < r**2
        if condition_1 and condition_2 :
            pass
        elif condition_1 :
            res += 1 
        elif condition_2 :
            res += 1 
    print(res)