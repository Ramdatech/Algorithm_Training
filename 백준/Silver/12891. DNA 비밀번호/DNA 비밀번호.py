import sys, heapq
t = sys.stdin.readline
n, m = map(int, t().split())
txt = t().strip()
ls = list(map(int, t().strip().split()))
stt, end = 0, m-1
res = [0]*4
for i in range(stt, end+1) :
    if txt[i] == "A" :
        res[0] += 1
    elif txt[i] == "C" :
        res[1] += 1
    elif txt[i] == "G" :
        res[2] += 1
    elif txt[i] == "T" :
        res[3] += 1

y = 0
while end < n :
    if all([x<=y for x, y in zip(ls, res)]) :
        y += 1
    if txt[stt] == "A" :
        res[0] -= 1
    elif txt[stt] == "C" :
        res[1] -= 1
    elif txt[stt] == "G" :
        res[2] -= 1
    elif txt[stt] == "T" :
        res[3] -= 1
    stt += 1
    end += 1
    if end < n :
        if txt[end] == "A" :
            res[0] += 1
        elif txt[end] == "C" :
            res[1] += 1
        elif txt[end] == "G" :
            res[2] += 1
        elif txt[end] == "T" :
            res[3] += 1

print(y)