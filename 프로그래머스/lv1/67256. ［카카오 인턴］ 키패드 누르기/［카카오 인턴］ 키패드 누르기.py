def distance(li) :
    for i in range(len(li)) :
        if li[i] == 0 :
            li[i] = 10
        else :
            li[i] -= 1
    num1, num3, goal = li
    return abs(num1//3-goal//3)+abs(num1%3-goal%3), abs(num3//3-goal//3)+abs(num3%3-goal%3)

def solution(numbers, hand):
    answer = ''
    hands = [10, 12]
    for i in numbers :
        a, b = distance(hands+[i])
        if i in [1, 4, 7] :
            answer += "L"
            hands[0] = i
        elif i in [3, 6, 9] :
            answer += "R"
            hands[1] = i
        elif i in [2, 5, 8, 0] :
            if (a == b and hand=="right") or a > b:
                answer += "R"
                hands[1] = i
            elif (a == b and hand=="left") or a < b:
                answer += "L"
                hands[0] = i
    return answer