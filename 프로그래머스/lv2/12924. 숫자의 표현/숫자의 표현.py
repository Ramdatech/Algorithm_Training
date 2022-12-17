def solution(n):
    answer=0
    x = 0
    for i in range(1, 101):
        x += i
        if n < x :
            break
        elif (n-x)%i == 0 :
            answer += 1
    return answer