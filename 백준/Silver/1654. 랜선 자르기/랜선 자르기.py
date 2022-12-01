import sys
import math
input = sys.stdin.readline

n,m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
pre, post = 1, max(ls)
while 1:
    sample = (pre+post)//2
    var = sum([x // sample for x in ls])
    if var >= m:
        pre = sample+1
    elif var < m:
        post = sample-1

    if pre > post :
        sample = post
        break
print(sample)