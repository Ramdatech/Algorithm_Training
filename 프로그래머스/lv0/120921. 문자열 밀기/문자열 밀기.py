def solution(A, B):
    answer = (A*2).find(B)
    if answer >0 :
        return len(A)-answer
    else :
        return answer