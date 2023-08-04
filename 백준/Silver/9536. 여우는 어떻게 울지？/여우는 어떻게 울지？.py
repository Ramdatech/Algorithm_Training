num = int(input())
for i in range(num):
    ls = []
    sigs = input().split()
    while 1 : 
        tmp = input().split(" goes ")
        if len(tmp) == 1 :
            break
        ls.append(tmp[1])
    print(*[x for x in sigs if x not in ls])