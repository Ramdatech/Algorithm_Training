import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, t().split())) for _ in range(n)]
x, y = 0, 0
def recur(m, ls) :
    global x, y
    tmp = sum(sum(ls, []))
    if tmp == 0 :
        x += 1
        return
    if tmp == m**2 :
        y += 1
        return

    m //= 2
    recur(m, [i[:m] for i in ls[:m]])
    recur(m, [i[m:] for i in ls[:m]])
    recur(m, [i[:m] for i in ls[m:]])
    recur(m, [i[m:] for i in ls[m:]])

recur(n, ls)
print(x)
print(y)