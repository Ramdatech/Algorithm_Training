def solution(a, b):
    for i in range(min([a,b]), 1, -1):
        if a%i == 0 and b%i == 0 :
            a, b = a//i, b//i
    while 1:
        if b%2 == 0 :
            b = b//2
        elif b%5 == 0 :
            b = b//5
        else :
            break
    return 1 if b == 1 else 2