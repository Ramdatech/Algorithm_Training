n = int(input())
scores = sorted(list(map(int, input().split())), reverse=True)
msk = [0.04, 0.11, 0.23, 0.40, 0.60, 0.77, 0.89, 0.96, 1.00]
cnt, cur = [0] * 9, 0
for i, chk in enumerate(msk):
    if cur >= n:
        break
    mx = int(chk * n)
    while cur < n and cur < mx:
        cnt[i] += 1
        cur += 1
    while cur < n and scores[cur] == scores[cur - 1]:
        cnt[i] += 1
        cur += 1
print(*cnt, sep="\n")