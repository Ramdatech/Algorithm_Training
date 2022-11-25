import sys
a = int(sys.stdin.readline())
i = 1
while a!=1 :
    i += 1
    if a%i == 0 :
        print(i)
        a = a//i
        i = 1