import sys
input = sys.stdin.readline
n = int(input().strip())
for _ in range(n) :
    t = input().strip()
    if len(t) % 2 == 1 or len(t) == 0:
        print('NO')
    else :
        s = 0
        e = 0
        for i in t[::-1]:
            if i == ")" :
                e += 1
            else :
                s += 1
            if s>e :
                e=-1
                break
        if s==e :
            print("YES")
        else :
            print("NO")