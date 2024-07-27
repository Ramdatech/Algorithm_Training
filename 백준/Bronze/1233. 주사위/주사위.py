def f(a, b, c):
    ls = [[0, i] for i in range(a+b+c+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            for k in range(1, c+1):
                ls[i+j+k][0] -= 1
    ls.sort()
    return ls[0][1]
print(f(*map(int, input().split())))