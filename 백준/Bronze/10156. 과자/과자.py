import sys
input = sys.stdin.readline
n,m,a = map(int, input().split())
if n*m-a >= 0 :
    print(n*m-a)
else : 
    print(0)