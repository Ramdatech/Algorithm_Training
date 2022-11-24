def solution(balls, share):
    answer = 1
    for i in range(share):
        answer *= balls-i
        answer /= share-i
    return int(round(answer,1))