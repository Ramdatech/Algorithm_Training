visit = []
def fs(pre, ls, num):
    global visit
    if len(pre) > num:
        return None
    for i in ls:
        temp = pre[:]
        templs = ls[:]
        if temp == [] or (temp[-1][1] == i[0]) :
            temp.append(i)
            templs.remove(i)
            fs(temp, templs, num)
            if len(temp) == num:
                visit.append(temp)
        
def solution(tickets):
    answer = []
    tickets = [['', "ICN"]] + tickets
    fs([], tickets, len(tickets))
    answer = sorted([["".join(y) if num == 0 else y[1] for num, y in enumerate(t)] for t in visit])
    return answer[0]