import math
def solution(progresses, speeds):
    answer = []
    mx = -1
    count = 0
    for i in zip(progresses, speeds) :
        x = math.ceil((100-i[0])/i[1])
        if x > mx : 
            mx = x
            answer.append(0)
            answer[-1] += 1
        else : 
            answer[-1] += 1
    return answer