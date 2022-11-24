def solution(arr, divisor): 
    return [-1] if sorted([x for x in arr if x%divisor == 0])==[] else sorted([x for x in arr if x%divisor == 0])