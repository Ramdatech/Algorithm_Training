import sys
input = sys.stdin.readline
n = int(input().strip())
res = []
for i in range(n) :
    a = int(input().strip())
    if a == 0 :
        res.pop(-1)
    else:
        res.append(a)
print(sum(res))