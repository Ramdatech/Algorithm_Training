import sys

def get_gcd(num1, num2):
    x, y = min(num1, num2), max(num1, num2)
    while 1 :
        if x%y == 0:
            return y
        else :
            x, y = y, x%y
    

t = sys.stdin.readline
n = int(t())
for _ in range(n):
    res = None
    ls = list(map(int,t().split()))
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            temp = get_gcd(ls[i], ls[j])
            if res == None or temp > res:
                res = temp
    print(res)