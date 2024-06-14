import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, list(t().strip()))) for _ in range(n)]

def recur(lst, m) :
    if len(set(sum(lst, []))) == 1 :
        return str(lst[0][0])
    a = recur([x[:m//2] for x in lst[:m//2]], m//2)
    b = recur([x[m//2:] for x in lst[:m//2]], m//2)
    c = recur([x[:m//2] for x in lst[m//2:]], m//2)
    d = recur([x[m//2:] for x in lst[m//2:]], m//2)
    return f"({a}{b}{c}{d})"

print(recur(ls, n))