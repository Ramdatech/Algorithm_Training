from collections import deque
def solution(priorities, location):
    answer = 1
    printed = [0] * len(priorities)
    printed[location] = 1
    printed = deque(printed)
    priorities = deque(priorities)
    while 1 :
        A, B = priorities.popleft(), printed.popleft()
        if A < max(priorities) :
            priorities.append(A)
            printed.append(B)
        elif A >= max(priorities) and B == 1 :
            break
        else :
            answer += 1
        
        if len(priorities) == 1:
            break

    return answer