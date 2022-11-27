import sys
input = sys.stdin.readline
n = int(input())
li = map(int,input().strip().split(" "))
res = [0, 0]
for i in li :
    if i  == 0 :
        res[0] = sum(res)
        res[1] = 0
    else :
        res[0] = sum(res)
        res[1] +=1
print(sum(res))