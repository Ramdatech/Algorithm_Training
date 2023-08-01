import sys
t = int(sys.stdin.readline())
print(' '.join(['long' for x in range(0, t, 4)]+['int']))