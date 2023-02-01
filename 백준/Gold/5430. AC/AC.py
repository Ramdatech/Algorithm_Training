import sys
t = sys.stdin.readline
n = int(t())
for _ in range(n) :
    command = t()
    nm = int(t())
    ls = eval(t())
    a = [0, 0, len(ls)]
    for i in list(command) :
        if i =='R' :
            a[0] ^= 1
        elif a[0]==0 and i=="D":
            a[1] += 1
        elif a[0]==1 and i=="D":
            a[2] -= 1
    if len(ls)-a[2]+a[1] > nm :
        print('error')
    else :
        ls = ls[a[1]:a[2]]
        print(str(ls).replace(" ", '') if a[0]==0 else str(ls[::-1]).replace(" ", ''))