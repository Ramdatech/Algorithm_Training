import sys

var1 = list(map(int,sys.stdin.readline().split()))
var2 = list(map(int,sys.stdin.readline().split()))

res = []
for i in var2:
    if var1[1] > i :
        res.append(str(i))
print(" ".join(res))