def solution(d, budget):
    if sum(d) <= budget :
        return len(d)
    
    d.sort()    
    for i in range(0,len(d)+1):
        if sum(d[:i]) > budget :
            return i-1