from collections import deque

def solution(maps):
    answer = 0
    direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    que = deque([[0, 0]])

    row, col = len(maps), len(maps[0])

    while que:
        pos = que.popleft()
        x, y = pos
        for d in direct:
            dx, dy = [sum(i) for i in list(zip(pos, d))]
            if 0 <= dx < row and 0 <= dy < col and maps[dx][dy] == 1:
                maps[dx][dy] = maps[x][y] + 1
                que.append([dx, dy])

    if maps[-1][-1] <= 1:
        return -1
    else :
        return maps[-1][-1]