def solution(sizes):
    answer = []
    res = sizes[:]
    a,b = list(zip(*res))
    a = list(a)
    b = list(b)
    answer.append(max(a)*max(b))
    for i in range(len(a)) :
        t = b.index(max(b))
        a[t], b[t] = b[t], a[t]
        answer.append(max(a)*max(b))
    return min(answer)