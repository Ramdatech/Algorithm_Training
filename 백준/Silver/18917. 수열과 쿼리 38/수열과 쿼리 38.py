import sys
t = sys.stdin.readline
n = int(t())
cx, cs = 0, 0
for _ in range(n):
    s, *a = t().split()
    match s:
        case '1':
            tmp = int(a[0])
            cs += tmp
        case '2':
            tmp = int(a[0])
            cs -= tmp
        case '3' :
            print(cs)
        case '4' :
            print(cx)
    if a :
        cx ^= int(a[0])