import sys
t = sys.stdin.readline
lst = [list(t().strip()) for _ in range(10)]
msk = {"X": 0, ".": 1}

def f(ls):    
    for i in range(10):
        for j in range(10):
            for t1, t2 in [(0, 1), (1, 0), (1, -1), (1, 1)]:
                L = [0, 0]
                if not (0<=i+4*t1<10 and 0<=j+4*t2<10) :
                    continue
                for x in range(5):
                    if ls[i+x*t1][j+x*t2] == "O":
                        break
                    L[msk[ls[i+x*t1][j+x*t2]]] += 1
                if sum(L) == 5 and L[0] == 4:
                    return 1
    return 0

print(f(lst))