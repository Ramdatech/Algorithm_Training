a, b = sorted(list(map(int, input().split())))
print(0 if b == a else b-a-1)
print(*[x for x in range(a+1, b)])