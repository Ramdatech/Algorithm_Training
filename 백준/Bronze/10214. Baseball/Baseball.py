import sys
t = sys.stdin.readline
n = int(t())
for _ in range(n):
    a, b = [sum(x) for x in zip(*[list(map(int, t().strip().split())) for _ in range(9)])]
    if a > b:
        print("Yonsei")
    elif a < b:
        print("Korea")
    else:
        print("Draw")