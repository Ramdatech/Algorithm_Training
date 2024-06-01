import sys
t = sys.stdin.readline
while 1 :
    n = int(t())
    if n == 0 : break
    print(sum([x for x in range(1, n+1)]))