T, M, N = map(int, input().split())
tab, stt = [], [1e12, [0, 0]]
for _ in range(T):
    tn, *tms = input().split()
    for t in map(int, tms[:-1]):
        L = [t, tn]
        for dt in [0, 60]:
            S=t+dt
            if S-M < stt[0] and M <= S :
                stt = [S-M, L]
        tab.append(L)
tab.sort()
print(tab[(tab.index(stt[1])+N)%len(tab)-1][1])