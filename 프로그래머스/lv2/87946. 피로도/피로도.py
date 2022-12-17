from itertools import permutations

def solution(k, dungeons):
    answer = -1
    for i in range(len(dungeons), -1, -1) :
        ls = list(permutations(dungeons, i))
        for j in ls :
            temp = int(k)
            for a, b in j :
                if temp >= a :
                    temp -= b
                else :
                    break
            else :
                if temp >= 0:
                    return i
    return 0