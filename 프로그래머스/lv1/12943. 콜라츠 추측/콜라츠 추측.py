def solution(num):
    count = 0 
    if num == 1 :
        return count
    while 1 :
        if num%2 == 0 : num /= 2
        elif num%2 != 0 : num = num*3 + 1
        count += 1 
        if count >= 500 :
            return -1
        elif num == 1 :
            return count