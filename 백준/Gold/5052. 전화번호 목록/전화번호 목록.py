import sys
t = sys.stdin.readline
n = int(t().strip())
for _ in range(n):
    m = int(t().strip())
    ls = sorted([t().strip() for _ in range(m)])
    for i in range(m-1):
        if ls[i] == ls[i+1][:len(ls[i])]:
            print('NO')
            break
    else:
        print('YES')