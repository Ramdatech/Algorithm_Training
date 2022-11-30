def solution(people, limit):
    answer = 0
    people.sort()
    pre, post = 0, len(people)-1
    while 1 :
            
        if people[pre] + people[post] <= limit:
            pre += 1
            post -= 1
        else :
            post -= 1
        answer += 1
                        
        if pre > post:
            break
            
    return answer