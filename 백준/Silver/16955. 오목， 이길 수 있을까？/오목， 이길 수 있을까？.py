import sys
t = sys.stdin.readline
lst = [list(t().strip()) for _ in range(10)]
msk = ["."] + ["X"] * 4

def f(ls):    
    for i in range(10):
        for j in range(10):
            if 4<=i+4<=9 and 0<=j-4<=5 and sorted([ls[i+x][j-x] for x in range(5)]) == msk:
                return 1
            if 4<=i+4<=9 and 4<=j+4<=9 and sorted([ls[i+x][j+x] for x in range(5)]) == msk :
                return 1
            if len(ls[i][j:j+5])==5 and sorted(ls[i][j:j+5]) == msk :
                return 1
            if 4<=i+4<=9 and sorted([ls[i+x][j] for x in range(5)]) == msk :
                return 1
    return 0

print(f(lst))