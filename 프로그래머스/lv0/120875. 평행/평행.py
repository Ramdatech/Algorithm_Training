def gradiant(li):
    li1 = li[0]
    li2 = li[1]
    return 1 if (li2[0]-li1[0]) == 0 else (li2[1]-li1[1])/(li2[0]-li1[0])
    
def solution(dots):
    answer = []
    for i in range(len(dots)):
        if gradiant((dots[i:]+dots[:i])[:2]) == gradiant((dots[i:]+dots[:i])[2:]):
            return 1
    return 0
    