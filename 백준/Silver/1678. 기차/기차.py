T, M, N = map(int, input().split())
tab = []
stt = [1e12, [0, 0]]
for _ in range(T):
    tn, *tms = input().split()
    tms = list(map(int, tms[:-1]))
    for t in tms :
        if t-M < stt[0] and t >= M :
            stt = [t-M, [t, tn]]
        if (t+60)-M < stt[0] and M <= t+60 :
            stt = [(t+60)-M, [t, tn]]
        tab.append([t, tn])
tab.sort()
print(tab[(tab.index(stt[1])+N)%len(tab)-1][1])