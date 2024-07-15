from collections import defaultdict
t = int(input())
res, cls = [], defaultdict(set)
for i in range(t):
    tmp = list(map(int, input().split()))
    res.append([tmp, i])
    for n,j in enumerate(tmp) :
        cls[(n,j)].add(i)
print(sorted([[-len(set(sum([list(cls[(n,j)]) for n, j in enumerate(ls)], []))), i] for ls, i in res])[0][1]+1)