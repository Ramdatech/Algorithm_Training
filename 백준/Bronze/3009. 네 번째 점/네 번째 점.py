import sys
input = sys.stdin.readline
res = []
for i in range(3) :
    res.append(list(map(int, input().strip().split())))

for i in range(3):
    dx = res[i][0] - res[i-1][0]
    dy = res[i][1] - res[i-1][1]
    if dx != 0 and dy != 0 :
        p1 = res[i]
        p2 = res[i-1]
        if [p1[0], p2[1]] in res :
            print(p2[0], p1[1])
        else :
            print(p1[0], p2[1])