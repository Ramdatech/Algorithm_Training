import sys
t = sys.stdin.readline
n = int(t())
for i in range(n) :
    dict = {}
    n1 = int(t())
    if n1 == 0 :
        print(0)
    else :
        for j in range(n1) :
            a, b = t().split()
            if b in dict.keys():
                dict[b] += 1
            else :
                dict[b] = 2
        print(eval('*'.join(map(str, dict.values())))-1)