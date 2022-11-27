def solution(babbling):
    answer = 0
    ls = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for idx, j in enumerate(ls):
            babbling[i] = babbling[i].replace(j, str(idx))
    
    for i in babbling : 
        if i.isdecimal() :
            if i.find("11") + i.find("22")+ i.find("33")+i.find("00") == -4 :
                answer += 1
            
    return answer