import sys
t = sys.stdin.readline
n = int(t())
tmp = [[x, x] for x in list(map(int, t().strip().split()))]
for _ in range(0, n-1) :
    a = list(map(int, t().strip().split()))
    tx = []
    for i, j in [[0, 2], [0, 3], [1, 3]] :
        x, y = zip(*tmp[i:j])
        tx.append((max(x), min(y)))
    tmp = [[w + tx[t][0], w + tx[t][1]] for t, w in enumerate(a)]

x, y = zip(*tmp)
print(max(x), min(y))