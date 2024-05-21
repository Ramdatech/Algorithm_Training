import sys
t = sys.stdin.readline
x, y = map(int, t().split())
z = y * 100 // x
stt, end = 1, x
if z >= 99:
    print(-1)
else :
    while stt < end:
        mid = (stt + end) // 2
        if (y + mid) * 100 // (x + mid) > z:
            end = mid
        else:
            stt = mid + 1
    print(stt)