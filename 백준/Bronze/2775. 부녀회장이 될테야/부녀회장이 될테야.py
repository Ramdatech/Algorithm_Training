import sys
t = sys.stdin.readline
a = int(t())
for _ in range(a) :
    k = int(t())
    n = int(t())
    li = [x+1 for x in range(n)]
    for _ in range(k) :
        li = [sum(li[:x+1]) for x in range(len(li))]
    print(li[n-1])