import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    while b//5 > 0 :
        b = b//5 + b%5
    res = str(a**b)[-1]
    if res == '0' :
        print(10)
    else :
        print(res)