def solution(denum1, num1, denum2, num2):
    denum1, num1, denum2, num2 = denum1*num2, num1*num2, denum2*num1, num2*num1
    answer = [denum1+denum2, num1]
    for i in range(max(answer)+1, 1, -1):
        if answer[0]%i == 0 and answer[1]%i == 0 :
            answer = [answer[0]//i, answer[1]//i]
    return answer