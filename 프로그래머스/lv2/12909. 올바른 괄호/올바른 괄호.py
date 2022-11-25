def solution(s):
    answer = [0, 0] 
    for i in s[::-1]:
        answer[i==")"] += 1
        if answer[0] > answer[1]:
            return False
    return answer[0] == answer[1]