def solution(board, moves):
    answer = 0
    board = [[y for y in list(x)[::-1] if y != 0] for x in zip(*board)]
    bucket = []
    for move in moves :   
        if bucket[-1:] == board[move-1][-1:] and bucket[-1:] != []:
            bucket.pop(-1)
            board[move-1].pop(-1)
            answer += 2
        else :
            if board[move-1][-1:] != [] :
                bucket.append(board[move-1][-1])
                board[move-1].pop(-1)

        
    return answer