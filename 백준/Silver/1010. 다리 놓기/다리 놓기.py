import sys
input = sys.stdin.readline
n = int(input().strip())
for _ in range(n) :
    n ,m = map(int,sys.stdin.readline().strip().split())
    for i in range(m-1, m-n, -1):
        m *= i
    for i in range(n-1, 0, -1) :
        n *= i
    print(m//n)