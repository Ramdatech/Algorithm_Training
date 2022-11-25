from collections import Counter
def solution(id_list, report, k):
    answer = {x:0 for x in id_list}
    report = [x.split() for x in set(report)]
    a, b = zip(*report)
    b = Counter(b)
    for idx, x in enumerate(report) :
        if b[x[1]] >= k :
            answer[x[0]] += 1
    return list(answer.values())