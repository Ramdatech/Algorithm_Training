def func(N):
    ans = 0
    dq = []
    while N > 0:
        ans *= 3
        if N & 1:
            dq.append(1)
        else:
            dq.append(0)
        N >>= 1

    exp = 1
    while dq:
        ans += dq.pop(0) * exp
        exp *= 3

    return ans

n = int(input())
res = [int(input()) for _ in range(n)]
for a in res :
    print(func(a))
