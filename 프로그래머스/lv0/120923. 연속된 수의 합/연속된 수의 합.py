def solution(num, total):
    return [int((total*2/num-(num-1))/2)+x for x in range(num)]