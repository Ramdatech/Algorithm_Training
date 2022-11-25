def solution(a, b, n):
    answer = 0
    while 1 :
        n, answer = (n//a)*b + n%a, (n//a)*b + answer
        if n < 2 or n//a == 0:
            break
    return answer