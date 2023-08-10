def f():
    return map(int, input().split())
a, b = f()
ls = list(f())
s, e = 0, b
res = [sum(ls[s:e])]
for i in range(a-b) : 
    res.append(res[-1]-ls[s]+ls[e])
    s+=1; e+=1
print(max(res))