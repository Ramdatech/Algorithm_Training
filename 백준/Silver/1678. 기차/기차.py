T, M, N = map(int, input().split())
tab = []
stt = [1e12, [0, 0]]
for _ in range(T):
    tn, *tms = input().split()
    tms = list(map(int, tms[:-1]))
    for t in tms :
        for dt in [0, 60]:
            if t+dt-M < stt[0] and M <= t+dt :
                stt = [t+dt-M, [t, tn]]
        tab.append([t, tn])
tab.sort()
print(tab[(tab.index(stt[1])+N)%len(tab)-1][1])