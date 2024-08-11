import sys
t = sys.stdin.readline
N, n = int(t()), 26
for i in range(N):
    cnt = [0]*n*2
    for c in t().strip(): cnt[ord(c)-97]+=1
    for c in t().strip(): cnt[ord(c)-97+n]+=1
    print(f"Case #{i+1}: {sum(abs(cnt[a]-cnt[a+n]) for a in range(n))}")