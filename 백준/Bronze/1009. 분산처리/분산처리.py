import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n) :
    a, b = input().split()
    while int(b)//5 > 0 :
        b = int(b)//5 + int(b)%5
    res = 1
    for _ in range(int(b)):
        res *= int(a)
        res = int(str(res)[-1])
    if res == 0 :
        print(10)
    else :
        print(res)