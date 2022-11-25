def solution(sizes):
    answer = []
    res = [[x,y] if x>=y else [y,x] for x,y in sizes]
    a,b = list(zip(*res))
    return max(a)*max(b)