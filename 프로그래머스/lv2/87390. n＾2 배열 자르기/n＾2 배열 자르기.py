def solution(n, left, right):
    answer = []
    for y in range(left//n+1, right//n+2) :
        answer += [y if x<=y else x for x in range(1, n+1)]
    return answer[left%n : right-n*(left//n)+1]