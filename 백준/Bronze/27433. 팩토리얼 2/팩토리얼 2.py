import sys
t = sys.stdin.readline
n = int(t())
res = 1
for i in range(2,n+1):
    res *= i
print(res)