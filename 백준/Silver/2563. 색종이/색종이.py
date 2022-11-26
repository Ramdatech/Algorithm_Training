import sys
input=sys.stdin.readline
a=[[0]*100 for _ in range(100)]
n=int(input())
for _ in range(n):
    k,l=map(int,input().split())
    for i in range(k,k+10):
        for j in range(l,l+10):
            a[i][j]=1
s=0
for row in a: s+=sum(row)
print(s)