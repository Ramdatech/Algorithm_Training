import sys
input = sys.stdin.readline
a, b = [int(input()) for _ in [1,2]]
res = [x for x in range(a, b+1) if round(x**0.5) == x**0.5]
if res :
    print(sum(res))
    print(res[0])
else :
    print(-1)