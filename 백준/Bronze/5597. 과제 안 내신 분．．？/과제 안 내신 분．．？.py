res = set(range(1, 31))
for _ in range(28):
    res.remove(int(input()))
res = list(res)
print(res[0])
print(res[1])