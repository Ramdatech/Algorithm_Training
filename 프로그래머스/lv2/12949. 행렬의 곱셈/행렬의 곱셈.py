def solution(arr1, arr2):
    answer = [[sum([a*b for a,b in zip(x, y)]) for y in zip(*arr2)] for x in arr1]
    return answer