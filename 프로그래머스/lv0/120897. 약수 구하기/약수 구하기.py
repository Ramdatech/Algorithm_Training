def solution(n):
    answer = [[x,n//x] for x in range(1, int(n**0.5)+1) if n%x == 0]
    answer = list(set(sum(answer, [])))
    return sorted(answer)