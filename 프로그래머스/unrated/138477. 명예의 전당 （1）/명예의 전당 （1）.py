def solution(k, score):
    answer = []
    scoreboard = []
    for i in score:
        scoreboard.append(i)
        scoreboard = sorted(scoreboard, reverse=True)[:k]
        answer.append(scoreboard[-1])
    return answer