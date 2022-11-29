import math
def solution(progresses, speeds):
    answer = []
    ls = [math.ceil((100-x[0])/x[1]) for x in zip(progresses, speeds)]
    mx = -1
    count = 0
    for x in ls :
        if x > mx : 
            mx = x
            answer.append(0)
            answer[-1] += 1
        else : 
            answer[-1] += 1
    return answer