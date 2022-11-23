def solution(n):
    answer = [1 for x in range(1,n+1) if n%x == 0]
    return int(sum(answer))