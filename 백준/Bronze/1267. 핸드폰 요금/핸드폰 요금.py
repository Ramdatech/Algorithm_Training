n, a, r = input(), map(int, input().split()), [0, 0]
for i in a :
    r = [r[j-1] + (i//(30*j)+1) * (5*(j+1)) for j in range(1,3)]
x, y = r
if x < y : print("Y", x)
elif x > y : print("M", y)
else : print("Y M", x)