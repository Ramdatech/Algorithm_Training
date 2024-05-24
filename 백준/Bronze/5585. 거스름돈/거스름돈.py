import sys
t = sys.stdin.readline
n = int(t())
n, res = 1000-n, 0
for i in [500, 100, 50, 10, 5, 1]:
    res += n//i
    n %= i
print(res)