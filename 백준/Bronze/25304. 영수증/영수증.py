i = input
X = int(i())
res = 0
for _ in range(int(i())):
    a, b = map(int,i().split())
    X -= a * b

if X :
    print("No")
else :
    print("Yes")