import sys, heapq
t = sys.stdin.readline
n = int(t())
ls = [list(t().strip()) for _ in range(n)]
for i in zip(*ls):
    if len(set(list(i))) != 1 :
        print("?", end="")
    else :
        print(i[0], end="")