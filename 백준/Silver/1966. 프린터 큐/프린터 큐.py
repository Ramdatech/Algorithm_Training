import sys
from collections import deque

def printer(priorities, location):
    answer = 1
    printed = [0] * len(priorities)
    printed[location] = 1
    printed = deque(printed)
    priorities = deque(priorities)
    while 1:
        A, B = priorities.popleft(), printed.popleft()
        if len(priorities) == 0 :
            break
        if A < max(priorities):
            priorities.append(A)
            printed.append(B)
        elif A >= max(priorities) and B == 1:
            break
        else:
            answer += 1

    return answer

input = sys.stdin.readline
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    ls = list(map(int, input().split()))
    print(printer(ls, y))