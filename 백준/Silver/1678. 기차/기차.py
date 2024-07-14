import bisect

T, M, N = map(int, input().split())

tab = {}
trn = []
for info in range(T):
    tn, *tms = input().split()
    tms = list(map(int, tms[:-1]))
    trn += tms
    tab[tn] = tms

res = sorted(trn)
last = None
idx = (bisect.bisect_left(res, M) + N) % len(trn) - 1
for i in tab :
    if res[idx] in tab[i] :
        print(i)
        break