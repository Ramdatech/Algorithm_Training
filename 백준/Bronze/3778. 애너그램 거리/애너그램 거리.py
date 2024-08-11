import sys
t = sys.stdin.readline
N, n = int(t()), 26
for i in range(N):
    cnt1, cnt2 = [0]*n, [0]*n
    for c in t().strip(): cnt1[ord(c)-97]+=1
    for c in t().strip(): cnt2[ord(c)-97]+=1
    print(f"Case #{i+1}: {sum(abs(x-y) for x,y in zip(cnt1, cnt2))}")