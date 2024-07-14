import bisect
T, M, N = map(int, input().split())
tab = []
for _ in range(T):
    tn, *tms = input().split()
    tms = list(map(int, tms[:-1]))
    for t in tms :
        tab.append([t, tn])
tab.sort()
print(tab[(bisect.bisect_left(list(zip(*tab))[0],M)+N)%len(tab)-1][1])