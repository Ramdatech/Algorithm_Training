import sys, math
input = sys.stdin.readline
a,b = map(int, input().split())
res = a*(b-1)
while 1 :
    res +=1
    avg = res/a
    if math.ceil(avg) == b :
        break
print(res)