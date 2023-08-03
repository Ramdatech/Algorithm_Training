a, b = sorted(list(map(int, input().split())))
ls = [x for x in range(a+1, b)]
print(len(ls))
print(*ls)