N = int(input())
for i in range(N):
    w1, w2, n = input(), input(), 26
    cnt1, cnt2 = [0]*n, [0]*n
    for c in w1: cnt1[ord(c)-97]+=1
    for c in w2: cnt2[ord(c)-97]+=1
    print(f"Case #{i+1}: {sum(abs(cnt1[j]-cnt2[j]) for j in range(n))}")