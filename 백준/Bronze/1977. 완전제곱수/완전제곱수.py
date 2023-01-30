import sys, math
input = sys.stdin.readline
a, b = [int(input()) for _ in [1,2]]
res = [x**2 for x in range(math.ceil(a**0.5), math.ceil(b**0.5)+1) if a<=x**2<=b]
if res :
    print(sum(res))
    print(res[0])
else :
    print(-1)