def solution(bin1, bin2):
    answer = sum([(2**idx)*int(x) for idx, x in enumerate(bin1[::-1])])
    answer += sum([(2**idx)*int(x) for idx, x in enumerate(bin2[::-1])])
    res = ['',answer]
    while 1 :
        res[0] += str(res[1]%2)
        res[1] = res[1]//2
        if res[1]==0 :
            break
    return res[0][::-1]