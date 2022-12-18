def diff(str1, str2):
    dt = {x:str1.count(x) for x in list(str1)}
    for alpha in list(str2) :
        if alpha in dt.keys() :
            dt[alpha] -= 1
        else :
            dt[alpha] = 1
    if sum(1 if abs(x)==1 else 0 for x in dt.values()) == 2 :
        return True
    else :
        return False

def fs(pre, post, ls, count, c):
    count += 1
    for i in ls :
        if i not in pre and diff(pre[-1], i) :
            temp = pre+[i]
            c = fs(temp, post, ls, count, c)
        if pre[-1] == post : 
            c.append(count)
            return c
    else :
        return c
    
def solution(begin, target, words):
    answer = fs([begin], target, words, -1, [])
    if answer == [] :
        return 0
    else :
        return min(answer)