def solution(num, k):
    if str(k) in str(num) : 
        return list(str(num)).index(str(k))+1
    else:
        return -1