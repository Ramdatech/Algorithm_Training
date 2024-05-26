import sys
t = sys.stdin.readline
n = list(t().strip())
m = list(t().strip())
for _ in range(len(m)):
    if m == n :
        print(1)
        break
    if m[-1] == "B" :
        m = m[:-1][::-1]
    elif m[-1] == "A" :
        m.pop()
else :
    print(0)