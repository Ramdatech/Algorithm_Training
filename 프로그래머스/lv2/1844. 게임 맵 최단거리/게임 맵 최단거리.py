from collections import deque

def solution(maps):
    answer = 0
    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    ls = deque()
    ls.append([0, 0])

    row, col = len(maps), len(maps[0])

    while ls:
        temp = ls.popleft()
        for d in delta:
            step = [sum(x) for x in list(zip(temp, d))]
            if 0 <= step[0] < row and 0 <= step[1] < col and maps[step[0]][step[1]] == 1:
                maps[step[0]][step[1]] = maps[temp[0]][temp[1]] + 1
                ls.append(step)

    if maps[-1][-1] <= 1:
        return -1
    else :
        return maps[-1][-1]