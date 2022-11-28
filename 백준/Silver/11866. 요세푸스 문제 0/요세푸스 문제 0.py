import sys
input = sys.stdin.readline
n, k = map(int,input().strip().split())
li = [x for x in range(1, n+1)]
res = []
while 1:
    if len(li) <= 1:
        res += list(map(str,li))
        break
    if len(li) == 1 :
        break
    elif len(li) >= k :
        res.append(str(li[k-1]))
        li = li[k:] + li[:k-1]
    else :
        t = k%len(li)
        res.append(str(li[t-1]))
        if t == 0 :
            li = li[:t-1]
        else :
            li = li[t:] + li[:t-1]
t = ", ".join(res)
print(f'<{t}>')