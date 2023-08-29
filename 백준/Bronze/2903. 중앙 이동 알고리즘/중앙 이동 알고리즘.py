num = int(input())
init = 2
res = init ** 2
for i in range(num):
    init = init+init-1
    res = init ** 2
print(res)