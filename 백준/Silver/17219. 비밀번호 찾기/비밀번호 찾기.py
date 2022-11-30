import sys
input = sys.stdin.readline
n, m = map(int,input().split())
ls = [input().strip().split() for _ in range(n)]
ls = {x[0] : x[1] for x in ls}
for i in range(m) :
    print(ls[input().strip()])