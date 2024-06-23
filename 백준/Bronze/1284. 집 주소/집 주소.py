while 1 :
    tmp = input()
    if tmp == '0' :
        break
    res = 1
    for i in tmp :
        if i == '0' :
            res += 4
        elif i == '1' :
            res += 2
        elif i == '2' :
            res += 3
        else :
            res += 3
        res += 1
    print(res)