def solution(brown, yellow):
    answer = []
    for i in range(1, int(yellow**0.5)+1):
        a,b = 0, 0
        if yellow%i == 0 :
            a, b = yellow//i, i
        if int((a+2)*(b+2)) == brown+yellow :
            return [a+2, b+2]