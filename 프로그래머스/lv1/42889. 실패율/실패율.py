def solution(N, stages):
    answer = []
    stages.sort()
    for i in range(1, N+1) :
        if i in stages :
            answer.append([i,stages.count(i)/len(stages[stages.index(i):])])
        else :
            answer.append([i,0])
    answer = list(zip(*sorted(answer, key=lambda x : x[1], reverse=True)))
    return answer[0]