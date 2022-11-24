def solution(arr1, arr2):
    return [[t1+t2 for t1, t2 in zip(x,y)] for x,y in zip(arr1, arr2)]