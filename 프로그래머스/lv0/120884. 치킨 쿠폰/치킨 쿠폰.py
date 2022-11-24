def solution(chicken):
    answer = 0
    while 1 :
        answer += chicken//10
        chicken = chicken//10 + chicken%10
        if chicken < 10 :
            break
    return answer