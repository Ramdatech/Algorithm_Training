import sys

def hanoi (n, start, goal, move, count):
    count += 1
    if n == 1 :
        move.append([start, goal])
        return move, count
    via = 6-(start + goal)
    move, count = hanoi(n-1, start, via, move, count)
    move.append([start, goal])
    move, count = hanoi(n-1, via, goal, move, count)
    return move, count

input = sys.stdin.readline
t = int(input())
a = hanoi(t, 1, 3, [], 0)
print(a[1])
for i in a[0]:
    print(*i)