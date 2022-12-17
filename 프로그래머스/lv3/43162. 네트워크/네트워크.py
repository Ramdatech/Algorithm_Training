def solution(n, computers):
    answer = []
    a = [[x+1 for x in range(len(computer)) if computer[x]==1] for computer in computers]
    ls = [set(a.pop(0))]
    index = 0
    while len(a) > 0 :
        temp = a.pop(0)
        if ls[index] & set(temp) != set() :
            ls[index] |= set(temp)
        else : 
            a.append(temp)
        if len(a) != 0 and set(sum(a,[])) & ls[index] == set():
            index += 1
            ls.append(set(a.pop(0)))
    return len(ls)