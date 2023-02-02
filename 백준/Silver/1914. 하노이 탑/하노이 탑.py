import sys

def hanoi (n, start, goal):
    if n == 1:
        print(start, goal)
        return None
    via = 6-(start + goal)
    hanoi(n-1, start, via)
    print(start, goal)
    hanoi(n-1, via, goal)


input = sys.stdin.readline
t = int(input())
print(2**t-1)
if not t > 20 :
    hanoi(t,1,3)