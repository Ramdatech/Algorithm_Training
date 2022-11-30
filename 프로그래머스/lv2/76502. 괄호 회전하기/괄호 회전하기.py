from collections import deque

def solution(s):
    answer = 0
    ls = deque(list(s))
    for i in range(len(s)) :
        ls.rotate(-1)
        res = ''.join(ls)
        while 1 :
            res = res.replace("{}", "").replace("[]", "").replace("()", "")
            if res == res.replace("{}", "").replace("[]", "").replace("()", "") :
                break
        if res == "":
            answer += 1
    return answer