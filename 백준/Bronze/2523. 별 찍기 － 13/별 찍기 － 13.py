import sys
t = sys.stdin.readline
n = int(t())
for i in range(1,2*n):
    if i > n:
        print("*"*(2*n-i))
    else :
        print("*"*i)