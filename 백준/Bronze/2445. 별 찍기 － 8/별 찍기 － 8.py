import sys
input = sys.stdin.readline
n = int(input())
a = ["*"*x + " "*2*(n-x) + "*"*x for x in range(1,n+1)]
print('\n'.join(a + a[:-1][::-1]))