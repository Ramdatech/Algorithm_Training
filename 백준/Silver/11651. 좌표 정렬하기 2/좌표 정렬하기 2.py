import sys
t = sys.stdin.readline
n = int(t())
res = []
for _ in range(n):
    res.append(list(map(int, t().split())))

for i in sorted(res, key = lambda x : (x[1], x[0])) :
    print(i[0], i[1])