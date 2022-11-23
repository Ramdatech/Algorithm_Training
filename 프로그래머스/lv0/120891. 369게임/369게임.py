def solution(order):
    return sum([1 for x in list(str(order)) if x in ['3', '6', '9']])