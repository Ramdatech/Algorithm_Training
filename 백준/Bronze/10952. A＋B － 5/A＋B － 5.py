import sys

while(1):
    var1 = list(map(int,input().split()))
    if sum(var1) == 0 :
        break
    else:
        print(sum(var1))
