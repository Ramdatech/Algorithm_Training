import sys
input = sys.stdin.readline
n, k = map(int, input().split())
if k == 0 :
    print(1)
else :
    x = [n, k]
    for i in range(1, k):
        n *= x[0]-i
        k *= x[1]-i
    print(n//k)