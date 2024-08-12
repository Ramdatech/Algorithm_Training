N, res = int(input()), []
if N :
    while N != 0:
        div=N%-2
        N//=-2
        if div<0:
            div+=2
            N+=1
        res+=[div]
    print(*res[::-1], sep='')
else :
    print(0)