N, S, R = map(int, input().split())
ls1, ls2 = [set(map(int, input().split())) for _ in range(2)]

tmp = ls1 & ls2
ls1 -= tmp
ls2 -= tmp

for team in ls2:
    if team - 1 in ls1:
        ls1.remove(team - 1)
    elif team + 1 in ls1:
        ls1.remove(team + 1)

print(len(ls1))