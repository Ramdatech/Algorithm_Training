import sys
t = sys.stdin.readline
n = int(t())
cx, cs = 0, 0
for _ in range(n):
    s, a, *b = (t()+" 0").split()
    a = int(a)
    match s:
        case '3' : print(cs)
        case '4' : print(cx)
        case _ :
            cs += a if s == "1" else -a
    if a : cx ^= a