import sys
t = sys.stdin.readline

while 1 :
    a, b, c = t().strip().split()
    if b == '0' and c == '0' : break

    if int(b) > 17 or int(c) >= 80 : print(a, "Senior")
    else : print(a, "Junior")