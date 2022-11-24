def solution(score):
    return [sorted([sum(x) for x in score], reverse=True).index(sum(x))+1 for x in score]