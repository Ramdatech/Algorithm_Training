import sys
t = sys.stdin.readline
temp = ''
res = 0
for i in list(t().strip()) :
    if i != temp :
        res += 10
        temp = i
    else :
        res += 5
print(res)