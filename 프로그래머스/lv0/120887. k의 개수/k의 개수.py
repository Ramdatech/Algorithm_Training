def solution(i, j, k):
    list = set([x for x in range(i, j+1)])
    answer = 0
    
    for t in range(i, j+1) :
        answer += sum([1 for x in str(t) if str(k)==x]) 
    
    return answer