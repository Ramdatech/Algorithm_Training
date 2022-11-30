def solution(prices):
    answer = []
    for i in range(len(prices)) :
        answer.append(0)
        for j in range(i+1, len(prices)) :
            if prices[i] <= prices[j] :
                answer[-1] += 1
            else :
                answer[-1] += 1
                break
    return answer