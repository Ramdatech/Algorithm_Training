import sys
t = sys.stdin.readline
K, N = t().strip().split()
l = len(K)
res = 0
for n, v in enumerate(list(K)) :
    if v.isdecimal() :
        tmp = int(v)
    else :
        tmp = int(ord(v)-55)
    res += tmp * (int(N)**(l-n-1))
print(res)