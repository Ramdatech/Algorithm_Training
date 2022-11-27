def solution(X, Y):
    answer = []
    lsx = [0] * 10
    lsy = [0] * 10
    if len(set(X)&set(Y)) ==0 : return '-1'
    elif set(X)&set(Y) == set(['0']) : return '0'
    for i in X :
        lsx[int(i)] += 1
    for i in Y :
        lsy[int(i)] += 1
    for idx,x in enumerate(list(zip(lsx, lsy))[::-1]):
        for i in range(min(x)):
            answer.append(str(9-idx))
    answer = "".join(answer)
    return answer