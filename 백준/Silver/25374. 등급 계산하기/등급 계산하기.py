n = int(input())
scr = sorted(list(map(int, input().split())), reverse=True)
msk = [int(x*n/100) for x in [4, 11, 23, 40, 60, 77, 89, 96, 100]]
cnt, cur = [0] * 9, 0
for i, mx in enumerate(msk):
    if cur >= n:
        break
    while cur < n and cur < mx:
        cnt[i] += 1
        cur += 1
    while cur < n and scr[cur] == scr[cur - 1]:
        cnt[i] += 1
        cur += 1
print(*cnt, sep="\n")