import sys
input = sys.stdin.readline
result = [0, 0]
for idx in range(5):
    ls = list(map(int,input().split()))
    if sum(ls) > result[1] :
        result[0] = idx+1
        result[1] = sum(ls)
print(*result)