import sys
t = sys.stdin.readline
n = int(t())
dp = [1, 0, 1, 1, 1, 1, 0]
print("SK" if dp[(n-1)%7] == 1 else "CY")