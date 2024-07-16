while 1 :
    age, *ls = map(int, input().split())
    if age==0 : break
    br = 1
    for t in range(0, len(ls), 2) :
        br=br*ls[t]-ls[t+1]
    print(br)