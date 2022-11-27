import sys
b = sys.stdin.readline
n = int(input().strip())
for _ in range(n):
    li = sorted(list(map(int, input().strip().split())))
    x = li[1]
    y = li[0]
    gcd = 0
    while 1 :
        if x%y == 0 :
            gcd = y
            break
        else :
            x, y = y,x%y
    
    print(int(li[0]*li[1]/gcd))