def solution(clothes):
    answer = 1
    legend = list(zip(*clothes))[1]
    ls = [legend.count(i) for i in set(legend)]
    for i in ls :
        answer *= i+1
    return answer-1