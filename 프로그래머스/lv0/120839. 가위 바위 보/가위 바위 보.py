def solution(rsp):
    rsp = list(rsp)
    for num, val in enumerate(rsp) :
        if val == '2' :
            rsp[num] = '0'
        elif val == '0' :
            rsp[num] = '5'
        elif val == '5' :
            rsp[num] = '2'
    return "".join(rsp)