def solution(s):
    answer = [0, 0]
    while 1 :
        val = len(s.replace("1", ""))
        s = bin(len(s)-val)[2:]
        answer[0] += 1
        answer[1] += val
        if s== "1":
            break
    return answer