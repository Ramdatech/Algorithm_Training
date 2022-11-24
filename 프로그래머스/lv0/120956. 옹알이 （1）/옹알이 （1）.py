def solution(babbling):
    li = ["aya", "ye", "woo", "ma" ]
    answer = 0
    for i in babbling :
        temp = i[:]
        for j in li :
            if len(temp) == len(temp.replace(j, " ")) + len(j) -1 :
                temp = temp.replace(j, " ")
            if set(list(temp)) == set([" "]) :
                answer += 1
                break
    return answer