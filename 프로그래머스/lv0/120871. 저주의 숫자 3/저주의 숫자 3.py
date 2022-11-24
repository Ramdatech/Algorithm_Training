def solution(n):
    return [x for x in range(300) if x%3 != 0 and str(x).find("3")<0][n-1]