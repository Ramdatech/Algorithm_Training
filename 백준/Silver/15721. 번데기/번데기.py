def f(a, b, c):
    tot, res = 0, 0
    for i in range(2, 100000):
        for j in [0, 1]*2+[0]*i+[1]*i :
            if j == c :
                res += 1
            if res == b :
                return tot%a
            tot += 1

print(f(*map(int, [input(), input(), input()])))