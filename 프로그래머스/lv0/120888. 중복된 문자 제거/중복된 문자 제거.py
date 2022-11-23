def solution(my_string):
    my_string = list(my_string)
    li = set(my_string)
    answer = []
    while 1 :
        a = my_string.pop(0)
        if a in li :
            answer.append(a)
            li.remove(a)
        if my_string == [] :
            break
    return ''.join(answer)