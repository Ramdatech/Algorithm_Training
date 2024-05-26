import sys
t = sys.stdin.readline
n = list(t().strip())
m = list(t().strip())
def w(n, m):
    for _ in range(len(m)):
        if m == n :
            return True
        if m[-1] == "B" :
            m = m[:-1][::-1]
        elif m[-1] == "A" :
            m.pop()
    return False
print(1 if w(n, m) else 0)