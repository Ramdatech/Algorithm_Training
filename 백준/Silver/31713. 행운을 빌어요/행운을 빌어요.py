import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, t().split())) for _ in range(n)]

def f(x, y):
    ans = 1e12

    for dx in range(300):
        nx = x+dx
        mn, mx = 3*nx, 4*nx

        if mn <= y <= mx:
            ans = min(ans, dx)
        elif y < mn:
            tmp = mn-y
            ans = min(ans, dx+tmp)
        elif y > mx:
            tmp = (y - mx + 2) // 3
            ny = y+tmp
            if mn <= ny <= mx:
                ans = min(ans, dx+tmp)
    return ans

for x,y in ls:
    print(f(x,y))