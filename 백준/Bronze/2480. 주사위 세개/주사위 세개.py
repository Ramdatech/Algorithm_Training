Prize = 0
ls = list(map(int, input().split()))
if len(set(ls)) == 1:
    Prize = ls[0] * 1000 + 10000
elif len(set(ls)) == 3:
    Prize = max(ls) * 100
else:
    Prize = sorted(ls)[1] * 100 + 1000
print(Prize)