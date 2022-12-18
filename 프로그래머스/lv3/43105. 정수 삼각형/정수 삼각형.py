dt = {}

def solution(triangle):
    answer = 0
    ls = [[-1 for y in x] for x in triangle]
    
    for n1, elements in enumerate(triangle) :
        for n2, i in enumerate(elements) :
            if n1-1 < 0 :
                ls[n1][n2] = triangle[n1][n2]
            elif n2-1 < 0 :
                ls[n1][n2] = ls[n1-1][n2] + triangle[n1][n2]
            elif n2+1 >= len(elements) :
                ls[n1][n2] = ls[n1-1][n2-1] + triangle[n1][n2]
            else :
                ls[n1][n2] = max(ls[n1-1][n2] + triangle[n1][n2], ls[n1-1][n2-1] + triangle[n1][n2])
    return max(ls[-1])