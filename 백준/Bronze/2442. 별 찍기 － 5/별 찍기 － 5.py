import sys
input = sys.stdin.readline
n = int(input())
res = []
for i in range(1,n+1) :
    res.append(" "*(n-i) + "*"*(2*i-1))
print("\n".join(res))