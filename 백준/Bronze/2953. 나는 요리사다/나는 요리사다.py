import sys
input = sys.stdin.readline
res = [0, 0]
for idx in range(5):
    ls = sum(list(map(int,input().split())))
    if ls > res[1] :
        res = [idx+1, ls]
print(*res)