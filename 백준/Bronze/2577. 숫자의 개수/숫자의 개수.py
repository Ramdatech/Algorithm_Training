res = 1
arr = [0 for i in range(10)]
for i in range(3):
    res *= int(input())

for i in range(10):
    print(str(res).count(str(i)))

