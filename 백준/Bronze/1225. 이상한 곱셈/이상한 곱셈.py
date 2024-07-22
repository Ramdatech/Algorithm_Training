x, y = [list(map(int, list(x))) for x in input().split()]
print(sum(i*j for i in x for j in y))