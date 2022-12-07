import sys
import math
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
b, c = map(int,input().split())
res = 0
for i in A :
    temp = i-b
    if temp <= 0:
        res += 1
        continue
    res += math.ceil(temp/c) + 1
print(res)