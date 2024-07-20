def f(N, m, M, T, R) :
    lim = m
    if M-m < T :
        return -1
    else :
        e=r=0
        while e < N :
            if m + T <= M :
                tmp = min((M-m)//T, N-e)
                e += tmp
                m += T*tmp
            else :
                m = max(m-R, lim)
                r += 1
        return e+r
print(f(*map(int, input().split())))