ls = [x for x in range(0, 21)]
for i in range(10):
    a, b = map(int, input().split())
    ls = ls[:a] + ls[a:b+1][::-1] + ls[b+1:]
print(*ls[1:])