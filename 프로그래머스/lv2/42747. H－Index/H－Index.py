def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for h, citation in enumerate(citations):
        if h >= citation :
            return h
    return len(citations)