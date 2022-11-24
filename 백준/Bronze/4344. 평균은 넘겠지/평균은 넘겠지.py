a = int(input())
for i in range(a):
    res = list(map(int,input().split()))[1:]
    average = sum(res)/len(res)
    
    count = 0
    for i in res:
        if average < i :
            count += 1
    print("{0:0.3f}%".format(count/len(res)*100))
    