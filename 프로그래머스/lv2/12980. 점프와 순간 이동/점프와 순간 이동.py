def solution(n):
    ans = 0
    res = n
    while 1 :
        if res % 2 == 0 :
            res /= 2
        else :
            res -= 1
            ans += 1
        if res == 0:
            break
    return ans