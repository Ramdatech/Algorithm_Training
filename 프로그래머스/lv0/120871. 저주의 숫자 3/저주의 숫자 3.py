def solution(n):
    x = 0
    res = []
    while 1:
        x += 1
        if x%3 != 0 and str(x).find("3")<0 :
            res.append(x)
        if len(res)==n:
            return x
