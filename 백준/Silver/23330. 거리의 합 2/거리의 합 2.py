import sys
t = sys.stdin.readline
n = int(t())
ls = sorted(list(map(int, t().strip().split())))
res = 0
for i in range(1, n) :
    res += (ls[i]-ls[i-1])*abs((n-i)**2-n*(n-i))
print(res*2)