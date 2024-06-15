import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, t().split())) for _ in range(n)]

def f(lst):
    res = []

    for x, y in lst:
        mn = float('inf')

        for ex in range(1001):
            total = x + ex
            mn_l = 3 * total
            mx_l = 4 * total

            if mn_l <= y <= mx_l:
                mn = min(mn, ex)
            elif y < mn_l:
                a_lv = mn_l - y
                mn = min(mn, ex + a_lv)
            elif y > mx_l:
                tmp_lv = (y - mx_l + 2) // 3
                n_lv = y + tmp_lv
                if 3 * total <= n_lv <= 4 * total:
                    mn = min(mn, ex + tmp_lv)
        res.append(mn)
    return res

for a in f(ls):
    print(a)