n = int(input())
a, b = 1, 0
for i in range(1, n+1) :
    a, b = b, a+b
print(a, b)