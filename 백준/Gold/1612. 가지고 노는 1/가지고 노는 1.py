import sys
t = sys.stdin.readline
n = int(t())

def f(n):
    res = 1 % n
    lt = 1
    vst = set()
    vst.add(res)

    while res != 0:
        res = (res * 10 + 1) % n
        lt += 1

        if res in vst:
            return -1
        vst.add(res)

    return lt

print(f(n))