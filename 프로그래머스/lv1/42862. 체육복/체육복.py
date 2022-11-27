def solution(n, lost, reserve):
    answer = []
    clothe = [1] * n
    
    for i in reserve :
        clothe[i-1] += 1
    for i in lost :
        clothe[i-1] -= 1
        
    for i in range(len(clothe)) :
        var = clothe.pop(-1)
        if i == 0 : 
            answer.append(var)
            continue
        if (var == 2 and answer[-1] == 0) or (var == 0 and answer[-1] == 2) :
            answer[-1] = 1
            answer.append(1)
        else :
            answer.append(var)
            
    return len(answer)-answer.count(0)