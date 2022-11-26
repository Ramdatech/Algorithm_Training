def solution(n):
    numbers = set([x for x in range(2, n+1)])
    for i in range(2, int(n**0.5)+1):
        numbers -= set([i*x for x in range(2, (n//i)+1)])
    
    return len(numbers)