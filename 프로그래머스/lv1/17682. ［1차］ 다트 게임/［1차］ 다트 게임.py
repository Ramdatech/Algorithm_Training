def solution(dartResult):
    SDT = {x:idx+1 for idx, x in enumerate("S D T".split())}
    answer = 0
    score = []
    dartResult = dartResult.replace("10", "!")
    for i in dartResult :
        if i.isdecimal() :
            score.append(int(i))
        elif i == "!" : 
            score.append(10)
        elif i.isalpha() : 
            score[-1] = score[-1]**SDT[i]
        elif i == "#" : 
            score[-1] = score[-1]*-1
        elif i == "*" :
            score[-2:] = [x*2 for x in score[-2:]]
    return sum(score)