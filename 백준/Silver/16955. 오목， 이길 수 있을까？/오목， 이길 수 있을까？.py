import sys
t = sys.stdin.readline
lst = [list(t().strip()) for _ in range(10)]
msk = ["."] + ["X"] * 4

def f(ls):    
    for i in range(10):
        for j in range(10):
            for t1, t2 in [(0, 1), (1, 0), (1, -1), (1, 1)]:
                tmp = []
                for x in range(5):
                    if not (0 <= i + x * t1 < 10 and 0 <= j + x * t2 < 10):
                        break
                    if ls[i + x * t1][j + x * t2] == "O":
                        break
                    tmp.append(ls[i + x * t1][j + x * t2])
                if len(tmp) == 5 and sorted(tmp) == msk:
                    return 1
    return 0

print(f(lst))