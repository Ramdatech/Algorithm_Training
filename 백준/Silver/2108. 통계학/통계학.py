import sys
t = sys.stdin.readline
n = int(t())
li = [0] * 8001
for _ in range(n):
    a = int(t())
    li[a+4000] += 1

res = [(idx-4000) for idx, x in enumerate(li) for _ in range(x)]
print(round(sum(res)/len(res)))
print(res[len(res)//2])
if li.count(max(li)) > 1:
    print(li.index(max(li), li.index(max(li))+1)-4000)
else :
    print(li.index(max(li))-4000)
print(max(res)-min(res))