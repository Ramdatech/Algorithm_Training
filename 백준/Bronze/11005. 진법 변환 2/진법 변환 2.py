import sys
t = sys.stdin.readline
K, N = map(int, t().strip().split())
ls = [(str(x), x) for x in range(10)]+[(chr(x+55), x) for x in range(10, 36)]
ls = {y:x for x, y in ls}
res = []
while K:
    res.append(ls[K%N])
    K = K//N
    if K < N and K != 0:
        res.append(ls[K])
        break
print(''.join(res)[::-1])
