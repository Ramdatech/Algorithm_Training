arr = []
for i in range(10):
    a = int(input())
    arr.append(a%42)
res = list(set(arr))
print(len(res))