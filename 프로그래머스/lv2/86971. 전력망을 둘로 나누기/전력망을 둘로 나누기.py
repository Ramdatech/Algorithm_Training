def solution(n, wires):
    answer = 10e6
    wires.sort()
    for i in range(1, len(wires)+1):
        ls = wires[:i-1] + wires[i:]
        a = set(ls.pop(0))
        while len(ls) > 0:
            temp = ls.pop(0)
            if len(a & set(temp)) > 0 :
                a |= set(temp)
            else :
                ls.append(temp)
            if len(set(sum(ls, [])) & a) == 0 :
                break
        if abs(len(a)*2-n) < answer :
            answer = abs(len(a)*2-n)
    return answer