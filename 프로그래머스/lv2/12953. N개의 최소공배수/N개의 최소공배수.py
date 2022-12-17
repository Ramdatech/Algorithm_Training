def uc(num1, num2) :
    a, b = max([num1, num2]), min([num1, num2])
    while b>0 :
        a, b = b, a%b
    return a

def solution(arr):
    answer = arr.pop(0)
    for i in arr :
        answer = answer*i/uc(answer,i)
    return answer 