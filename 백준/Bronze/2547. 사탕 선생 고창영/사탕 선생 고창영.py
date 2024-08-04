import sys
t = sys.stdin.readline
n = int(t())
t()
for _ in range(n):
    m = int(t())
    if sum(int(t()) for x in range(m)) % m == 0 :
        print("YES")
    else :
        print("NO")
    t()