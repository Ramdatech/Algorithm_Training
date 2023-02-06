import sys
t = sys.stdin.readline
a, b = map(int, t().split())
if b == 0 :
    print(1)
else :
    res = (eval('*'.join(map(str,range(a, a-b, -1)))))//eval('*'.join(map(str,range(b, 0, -1))))
    print(res % 10007)