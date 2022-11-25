b = int(input())
def eq(i) :
    return int((i ** 2 + i) * 0.5)
i = 0
a = 0
while b>a:
    i += 1
    a = eq(i)

if i%2 != 0 :
    print(f"{-b+a+1}/{b-(a-i)}")
else :
    print(f"{b-(a-i)}/{-b+a+1}")