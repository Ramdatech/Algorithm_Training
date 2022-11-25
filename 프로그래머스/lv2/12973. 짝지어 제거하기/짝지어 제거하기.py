def solution(s):
    answer = []
    for i in s :
        if answer[-1:] == [i] and answer != [] :
            answer.pop(-1)
        else :
            answer.append(i)
    return int(len(answer)==0)