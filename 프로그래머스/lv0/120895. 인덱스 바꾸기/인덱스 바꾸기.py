def solution(my_string, num1, num2):
    t = my_string
    t = t[:num1] + t[num2] + t[num1+1:num2] + t[num1] + t[num2+1:]
    return t