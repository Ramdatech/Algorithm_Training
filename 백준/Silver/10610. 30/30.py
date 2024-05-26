import sys
t = sys.stdin.readline
n = list(t().strip())
if '0' in n and sum(map(int, n)) % 3 == 0:
    print(''.join(sorted(n, reverse=True)))
else:
    print(-1)