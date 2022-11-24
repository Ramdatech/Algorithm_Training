def solution(board):
    lis = [[2] * (len(board[0])+2)]
    board = lis + board + lis
    for row in range(1, len(board)-1):
        board[row] = [2] + board[row] + [2]
    for row in range(1, len(board)):
        for col in range(len(board[row])) :
            if board[row][col] == 1 :
                for i in range(col-1, col+2) :
                    for j in range(row-1, row+2) :
                            board[j][i] = 1 if board[j][i] == 1 else 2 if board[j][i] == 0 else ""
    return sum(board,[]).count(0)
    