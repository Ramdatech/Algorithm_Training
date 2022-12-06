import sys
input = sys.stdin.readline
res = [0, 0]
for idx in range(5):
    ls = list(map(int,input().split()))
    if sum(ls) > res[1] :
        res = [idx+1, sum(ls)]
print(*res)