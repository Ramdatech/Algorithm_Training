def f(a, b, c):
    ls = [[0, i] for i in range(a+b+c+1)]
    for i in range(a):
        for j in range(b):
            for k in range(c):
                ls[i+j+k+3][0] -= 1
    ls.sort()
    return ls[0][1]
print(f(*map(int, input().split())))