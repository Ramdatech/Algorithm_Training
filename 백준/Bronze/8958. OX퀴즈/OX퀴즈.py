a = int(input())
for i in range(a):
    res = input().split("X")
    var = 0
    for j in res :
        for t in range(len(j)+1):
            var += t
    print(var)