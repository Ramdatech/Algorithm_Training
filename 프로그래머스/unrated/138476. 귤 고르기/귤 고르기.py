from collections import Counter

def solution(k, tangerine):
    li = Counter(tangerine).most_common()
    answer = [0, 0]
    for i in li :
        if answer[0] < k :
            answer[0] += i[1]
            answer[1] += 1
    return answer[1]