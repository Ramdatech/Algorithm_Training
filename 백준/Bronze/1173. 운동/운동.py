N, m, M, T, R = map(int, input().split())
lim = m
if M-m < T :
    print(-1)
else :
    cnt=res=0
    while cnt < N :
        if m + T <= M :
            cnt += 1
            m += T
        else :
            m = max(m-R, lim)
        res += 1
    print(res)