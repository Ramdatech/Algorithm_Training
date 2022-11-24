def solution(a, b):
    day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    answer = d[(sum(day[:a]) + b)%7]
    return answer