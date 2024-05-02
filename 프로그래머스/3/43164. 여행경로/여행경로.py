from collections import deque

def solution(tickets):
    tickets = [x+[idx] for idx, x in enumerate(tickets)]
    que = deque([[x[1], [x], x[:2]] for x in tickets if x[0] == "ICN"])
    res = []
    while que : 
        pos, hist, path = que.popleft()
        if len(hist) == len(tickets) :
            res.append(path)
        tics = [i for i in tickets if i[0] == pos and i not in hist]
        for i in tics : 
            que.append([i[1], hist+[i], path+[i[1]]])
    return sorted(res)[0]