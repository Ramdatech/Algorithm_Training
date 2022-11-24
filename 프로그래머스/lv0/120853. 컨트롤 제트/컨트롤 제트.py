def solution(s):
    answer = []
    for i in s.split():
        if i=="Z" and answer != [] :
            answer.pop(-1)
        else :
            answer.append(int(i))
    return sum(answer)