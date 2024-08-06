n, *ls = map(int, input().split())
a, b = sorted(ls)
mx = 0
while 1 :
    mx += 1
    if a == b :
        break
    a = (a+1)//2
    b = (b+1)//2
print(mx-1)