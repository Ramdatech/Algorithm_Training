def solution(array, n):
    array.sort()
    answer = 0
    count = 100
    for i in array:
        if count > abs(i-n) :
            count = abs(i-n)
            answer = i
    return answer