import sys
a = sys.stdin.readline().strip().lower()
b = list(set(a))
res = [0, 0]
for i in b : 
    temp = a.count(i)
    if temp > res[0] :
        res[0] = temp
        res[1] = i
    elif temp == res[0] :
        res[1] = "?"
print(res[1].title())