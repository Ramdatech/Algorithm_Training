def solution(arr1, arr2):
    answer = []
    arr2 = list(zip(*arr2))
    
    for ar1 in range(len(arr1)) :
        temp = []
        for ar2 in range(len(arr2)) :
            res = 0
            for mult in range(len(arr2[ar2])):
                res += arr1[ar1][mult] * arr2[ar2][mult]
            temp.append(res)
        answer.append(temp)
    return answer