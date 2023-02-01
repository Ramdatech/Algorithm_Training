import sys
t = sys.stdin.readline
a = t()
print(sum([a*b for a, b in zip(sorted(list(map(int, t().split()))), sorted(list(map(int, t().split())))[::-1])]))