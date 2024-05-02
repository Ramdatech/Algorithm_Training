def solution(br, yl):
    s = br+yl
    for i in range(1, int(s**0.5)+1) :
        if s%i == 0 :
            a, b = s//i, i
            if (a-2)*(b-2) == yl:
                return [a, b]