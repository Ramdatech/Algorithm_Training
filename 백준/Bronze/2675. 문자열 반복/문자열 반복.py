import sys
a = sys.stdin.readline()
for _ in range(int(a)):
    n, d = sys.stdin.readline().split()
    print(''.join([x*int(n) for x in d]))