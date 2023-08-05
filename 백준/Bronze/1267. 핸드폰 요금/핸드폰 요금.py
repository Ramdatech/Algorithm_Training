import math
n, a, r = input(), map(int, input().split()), [0, 0]
for i in a :
    r = [r[j-1] + math.ceil(i/(30*j) if i/(30*j)!=int(i/(30*j)) else i/(30*j)+1) * (5*(j+1)) for j in range(1,3)]
if r[0] < r[1] : print("Y", r[0])
elif r[0] > r[1] : print("M", r[1])
else : print("Y M", r[0])