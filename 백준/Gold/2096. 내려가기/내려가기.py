import sys
t = sys.stdin.readline
n = int(t())
tmp = [[x, x] for x in list(map(int, t().strip().split()))]
for _ in range(0, n-1) :
    a = list(map(int, t().strip().split()))
    tx = []
    for i in [[0, 1], [0, 1, 2], [1, 2]] :
        x, y = zip(*[tmp[j] for j in i])
        tx.append((max(x), min(y)))
    tmp = [[a[t] + tx[t][0], a[t] + tx[t][1]] for t in range(3)]

x, y = zip(*tmp)
print(max(x), min(y))