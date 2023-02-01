import sys
t = sys.stdin.readline
a = t()
print(*sorted(list(set(map(int,t().split())))))