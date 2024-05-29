import sys
t = sys.stdin.readline
n = int(t())
ls = [(x, i) for i, x in enumerate(list(map(int, t().split())))]
res = [0]*n
hist = []
for i in range(n):
    if hist == [] :
        hist.append(ls.pop())
    else :
        tmp = ls.pop()
        if tmp[0] >= hist[-1][0] :
            for j in range(len(hist)):
                if hist[-1][0] > tmp[0] :
                    break
                res[hist.pop()[1]] = tmp[1]+1
        hist.append(tmp)
print(*res)