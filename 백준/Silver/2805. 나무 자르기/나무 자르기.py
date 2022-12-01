import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int,input().split())
ls = list(map(int,input().strip().split()))
ct = Counter(ls)
start, end = 1, max(set(ls))
while 1:
    temp = 0
    mid = (start+end)//2
    for key, val in ct.items():
        if key > mid :
            temp += (key-mid)*val
    if temp < m :
        end = mid
    else :
        start = mid+1
    if start >= end :
        print(end-1)
        break