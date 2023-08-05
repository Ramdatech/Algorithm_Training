import math
n = input()
a = map(int, input().split())
res = [0, 0]
for i in a :
    res = [res[j] + math.ceil(i/(30*(j+1)) if i/(30*(j+1))!=int(i/(30*(j+1))) else i/(30*(j+1))+1) * (5*(j+2)) for j in range(2)]
if res[0] < res[1] :
    print("Y", res[0])
elif res[0] == res[1] :
    print("Y M", res[0])
else :
    print("M", res[1])