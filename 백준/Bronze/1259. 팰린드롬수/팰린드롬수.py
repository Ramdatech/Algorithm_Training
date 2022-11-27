while 1 :
    n = input()
    if n == '0' :
        break
    if n[::-1] == n :
        print("yes")
    else :
        print('no')