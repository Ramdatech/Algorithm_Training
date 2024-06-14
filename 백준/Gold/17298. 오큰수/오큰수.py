import sys
t = sys.stdin.readline
n = int(t())
ls = list(map(int, t().strip().split()))
res = []
que = []
while ls :
    tmp = ls.pop()
    if not que :
        res.append(-1)
        que.append(tmp)
    else :
        while que and que[-1] <= tmp :
            que.pop()
        if que :
            res.append(que[-1])
        else :
            res.append(-1)
        que.append(tmp)

print(*res[::-1])