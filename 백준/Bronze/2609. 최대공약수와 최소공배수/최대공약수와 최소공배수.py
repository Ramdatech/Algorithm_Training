import sys
b = sys.stdin.readline
n = sorted(list(map(int, input().strip().split())))
x = n[1]
y = n[0]
gcd = 0
while 1 :
    if x%y == 0 :
        gcd = y
        break
    else :
        x, y = y,x%y

print(gcd)
print(int(n[0]*n[1]/gcd))