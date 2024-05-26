import sys
t = sys.stdin.readline
n = list(t().strip())
m = list(t().strip())
for i in range(len(m)):
    if m == n :
        print(1)
        break
    if m[-1] == "B" :
        m.pop()
        m = m[::-1]
    elif m[-1] == "A" :
        m.pop()
else :
    print(0)