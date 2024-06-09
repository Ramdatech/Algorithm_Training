import sys
t = sys.stdin.readline
n = int(t())
ls = sorted(list(map(int, t().strip().split())))
print(sum([(ls[i]-ls[i-1])*abs((n-i)**2-n*(n-i)) for i in range(1, n)])*2)