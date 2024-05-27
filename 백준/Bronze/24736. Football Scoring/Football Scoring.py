import sys
t = sys.stdin.readline
for _ in range(2) :
    tmp = list(map(int, t().split()))
    print(sum([x*y for x, y in zip(tmp, [6, 3, 2, 1, 2])]))