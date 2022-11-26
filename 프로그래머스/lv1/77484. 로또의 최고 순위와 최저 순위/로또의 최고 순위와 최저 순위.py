def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    return [rank[len(set(win_nums) & set(lottos))+lottos.count(0)], rank[len(set(win_nums) & set(lottos))]]