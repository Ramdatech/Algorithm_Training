res = sorted([int(input()) for _ in range(4)])[::-1][:3]
res2 = sorted([int(input()) for _ in range(2)])[-1]
print(sum(res)+res2)