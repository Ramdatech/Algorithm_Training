import sys
t = sys.stdin.readline
n = int(t().strip())
for _ in range(n) :
    a = t().strip()
    print(f"{a[0]}{a[-1]}")