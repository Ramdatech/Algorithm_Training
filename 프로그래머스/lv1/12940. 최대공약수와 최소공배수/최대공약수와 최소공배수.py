def solution(n, m):
    mult = n*m
    if n < m : n,m = m,n
    gcd = 0
    while 1 :
        n, m = m, n%m
        if m == 0 :
            gcd = n
            break
    return [gcd,mult/gcd]