import sys
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [int(t()) for _ in range(n)]

stt, end = 0, max(ls) * m
while stt < end:
    mid = (stt + end) // 2
    tmp = sum(mid // l for l in ls)
    if tmp >= m:
        end = mid
    else:
        stt = mid + 1
print(stt)