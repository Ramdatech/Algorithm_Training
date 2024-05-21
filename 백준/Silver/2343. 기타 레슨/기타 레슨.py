import sys
t = sys.stdin.readline
n, m = map(int, t().split())
ls = list(map(int, t().split()))
s, e = max(ls), sum(ls)
while s < e:
    mid = (s+e)//2
    cnt, tmp = 1, 0
    for i in ls:
        if tmp+i <= mid:
            tmp += i
        else:
            cnt += 1
            tmp = i
    if cnt <= m:
        e = mid
    else:
        s = mid+1
print(s)