import sys
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [list(t().strip()) for _ in range(n)]
mx = 1
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bit(alpha):
    return 1 << ord(alpha)-65

vst = set((0, 0, bit(ls[0][0])))

def rec(x, y, lng, cnt) :
    global mx
    for dx, dy in dirs :
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m :
            if not bit(ls[nx][ny]) & lng and (nx, ny, lng | bit(ls[nx][ny])) not in vst :
                mx = max(mx, cnt+1)
                rec(nx, ny, lng | bit(ls[nx][ny]), cnt+1)
                vst.add((nx, ny, lng | bit(ls[nx][ny])))

rec(0, 0, bit(ls[0][0]), 1)
print(mx)