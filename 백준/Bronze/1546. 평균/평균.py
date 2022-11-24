import sys
a = int(input())

res = list(map(int,input().split()))

RES = 0
for i in res :
    RES += i/max(res) * 100 

print(RES/len(res))