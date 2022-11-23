a = list(map(int, input().split()))
a_rel = [a.count(x) for x in a]
if 3 in a_rel :
    res = 10000 + a[0]*1000
elif 2 in a_rel :
    res = 1000 + a[a_rel.index(2)]*100
else :
    res = max(a) * 100
print(res)