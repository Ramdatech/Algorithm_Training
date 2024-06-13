import sys
t = sys.stdin.readline
a, b, c = [t().strip() for _ in range(3)]
print(int(a)+int(b)-int(c))
print(int(a+b)-int(c))