import sys
input = sys.stdin.readline
n = int(input().strip())

ot = 1
while(1):
    if n <= 2 :
        print(n)
        break
    ot *= 2
    if ot >= n :
        print((n-ot//2)*2)
        break