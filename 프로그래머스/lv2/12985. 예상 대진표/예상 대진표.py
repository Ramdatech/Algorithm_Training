def solution(n,a,b):
    answer = 0
    while 1 :
        a, b = a//2 if a%2 == 0 else (a+1)//2 , b//2 if b%2 == 0 else (b+1)//2
        if a==b :
            answer += 1
            break
        else :
            answer += 1

    return answer