import math
def solution(n):
    a = math.sqrt(n)
    answer = 1 if a == int(a) else 2
    return answer