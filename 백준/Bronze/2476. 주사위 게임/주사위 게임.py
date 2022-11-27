import sys
t = sys.stdin.readline
n = int(t())
res = []
for _ in range(n):
    li = list(map(int, t().strip().split()))
    if li.count(li[0]) == 3 :
        res.append(10000 + li[0] * 1000)
    elif len(set(li)) == 3:
        res.append(max(li) * 100)
    else :
        res.append(1000 + (sum(li) - sum(set(li))) * 100)
print(max(res))