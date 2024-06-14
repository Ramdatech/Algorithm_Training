import sys, math
t = sys.stdin.readline
ls = [list(map(int,t().split())) for _ in range(3)]

p_ls = [(ls[i],ls[j]) for i in range(3) for j in range(i+1, 3)]
if len(set([(p2[1]-p1[1])/(p2[0]-p1[0]) if p2[0]-p1[0] != 0 else 0 for p1, p2 in p_ls])) == 1 :
    print("X")
    sys.exit()

w_ls = [(abs(x[0]-y[0])**2 + abs(x[1]-y[1])**2)**0.5 for x, y in p_ls]

w_ls = []
a_ls = []
for i in range(3) :
    ws = [(abs(ls[i][0]-ls[tg][0])**2 + abs(ls[i][1]-ls[tg][1])**2)**0.5 for tg in range(3) if tg != i]
    v1 = [ls[tg] for tg in range(3) if tg != i]
    v1, v2 = [v1[0][0]-ls[i][0], v1[0][1]-ls[i][1]], [v1[1][0]-ls[i][0], v1[1][1]-ls[i][1]]
    D = v1[0]*v2[0] + v1[1]*v2[1]
    angle = math.acos(max(-1, min(1, D/(ws[0]*ws[1]))))
    a_ls.append(math.degrees(angle))
    w_ls += ws

match len(set(w_ls)) :
    case 1 :
        print("JungTriangle")
    case 2 :
        if max(a_ls) > 90 :
            print("Dunkak2Triangle")
        elif max(a_ls) == 90 :
            print("Jikkak2Triangle")
        else :
            print("Yeahkak2Triangle")
    case 3 :
        if max(a_ls) > 90 :
            print("DunkakTriangle")
        elif max(a_ls) == 90 :
            print("JikkakTriangle")
        else :
            print("YeahkakTriangle")