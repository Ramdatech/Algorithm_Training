def solution(survey, choices):
    answer = ""
    dicti = {x:0 for x in "R T C F J M A N".split()}
    for i,j in zip(survey, choices) :
        dicti[i[j-4>0]] += abs(j-4)
    for i,j in "RT CF JM AN".split():
        if dicti[i] >= dicti[j] :
            answer += i
        elif dicti[i] < dicti[j] :
            answer += j
    return answer