res = [0]
for i in range(4) :
    ls = [[-1, +1], list(map(int, input().split()))]
    [res.append(res[-1]+a*b) for a, b in zip(*ls)]
print(max(res))