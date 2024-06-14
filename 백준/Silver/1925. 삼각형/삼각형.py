import sys, math
t = sys.stdin.readline
ls = [list(map(int,t().split())) for _ in range(3)]
p_ls = [(ls[i],ls[j]) for i in range(3) for j in range(i+1, 3)]
if len(set([(p2[1]-p1[1])/(p2[0]-p1[0]) if p2[0]-p1[0] != 0 else 0 for p1, p2 in p_ls])) == 1 :
    print("X")
    sys.exit()
w_ls = []
a_ls = []
for i in range(3) :
    x, y = ls[i]
    v1, v2 = [ls[tg] for tg in range(3) if tg != i]
    v1, v2 = [v1[0]-x, v1[1]-y], [v2[0]-x, v2[1]-y]
    w1, w2 = (v1[0]**2 + v1[1]**2)**0.5, (v2[0]**2 + v2[1]**2)**0.5
    a_ls.append(math.degrees(math.acos(max(-1, min(1, (v1[0]*v2[0] + v1[1]*v2[1])/(w1*w2))))))
    w_ls += [w1, w2]
res = ""
lg = len(set(w_ls))
if lg == 1 :
    res += "Jung"
else :
    if max(a_ls) > 90:
        res += "Dunkak"
    elif max(a_ls) == 90:
        res += "Jikkak"
    else:
        res += "Yeahkak"
    if lg == 2 : res += "2"
print(res+"Triangle")