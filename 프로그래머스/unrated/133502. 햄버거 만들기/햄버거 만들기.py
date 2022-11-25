def solution(ingredient):
    answer = 0
    burger = []
    for i in ingredient :
        if burger[-3:]+[i] == [1,2,3,1]  :
            burger.pop(-1)
            burger.pop(-1)
            burger.pop(-1)
            answer += 1
        else :
            burger.append(i)
    return answer