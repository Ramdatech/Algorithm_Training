def solution(numbers, target):
    answer = [[0]]
    for i in numbers :
        temp = []
        for j in answer[-1] :
            temp.append(j-i)
            temp.append(j+i)
        answer.append(temp)
    return answer[-1].count(target)