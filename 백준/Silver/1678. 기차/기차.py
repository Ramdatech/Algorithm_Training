import bisect
T, M, N = map(int, input().split())
tab = {}
for _ in range(T):
    tn, *tms = input().split()
    tms = list(map(int, tms[:-1]))
    for t in tms :
        tab[t] = tn
idx = (bisect.bisect_left(sorted(list(tab.keys())), M) + N) % len(tab) - 1
print(tab[sorted(list(tab.keys()))[idx]])