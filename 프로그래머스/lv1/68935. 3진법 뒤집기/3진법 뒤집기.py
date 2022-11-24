def solution(n):
    answer = ""
    while 1 :
        answer += str(n%3)
        n = n//3
        if n == 0 :
            break
        
    return sum([int(i)*(3**idx) for idx, i in enumerate(answer[::-1])])