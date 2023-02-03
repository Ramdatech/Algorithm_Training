import sys
def gcd(num1, num2):
    x, y = num1, num2
    while 1 :
        if x%y == 0:
            return y
        else :
            x, y = y, x%y
t = sys.stdin.readline
n = int(t())
for _ in range(n):
    res = -1
    ls = sorted(list(map(int,t().split())))
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            temp = gcd(ls[i], ls[j])
            if temp > res:
                res = temp
    print(res)