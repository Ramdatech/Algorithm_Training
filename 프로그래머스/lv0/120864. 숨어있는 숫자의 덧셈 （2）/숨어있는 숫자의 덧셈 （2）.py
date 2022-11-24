def solution(my_string):
    answer = 0
    idx = 0
    while 1:
        if my_string[idx].isdigit() :
            temp = max([my_string[idx:idx+x] for x in range(1, 5) if my_string[idx:idx+x].isdigit()])
            idx += len(temp)
            answer += int(temp)
        else :
            idx += 1
        if len(my_string) <= idx :
            break
            
    return answer