def solution(n):
    if n == 0 :
        return 0
    answer = set([1, n])
    for i in range(2, n):
        if n%i == 0 :
            answer.add(i)
    return sum(answer)