import sys
t = sys.stdin.readline
n = int(t())

def P(tmpls, s) :
    t = "." if s == 0 else "#"
    while tmpls :
        if set(tmpls[-1]) == set(t) :
            tmpls.pop()
        else :
            return tmpls
    return tmpls


for _ in range(n) :
    a, b = map(int, t().strip().split())
    ls = P([list(t().strip()) for _ in range(a)], 0)
    ls = P(ls[::-1], 0)
    ls = P([list(x) for x in zip(*ls)], 0)
    ls = P(ls[::-1], 0)

    if ls == [] or len(ls) != len(ls[0]) or [ls[0][0], ls[-1][-1], ls[0][-1], ls[-1][0]].count("#") != 3 :
        print(0)
        continue

    ls = P(ls, 1)
    ls = P(ls[::-1], 1)
    ls = P([list(x) for x in zip(*ls)], 1)
    ls = P(ls[::-1], 1)

    if ls == [] or set(sum(ls, [])) != set(".") or len(ls) != len(ls[0]):
        print(0)
        continue

    print(1)