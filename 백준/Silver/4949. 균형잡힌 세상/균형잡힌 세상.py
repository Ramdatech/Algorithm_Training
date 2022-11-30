import sys
input = sys.stdin.readline
text = ['(', ')', '[', ']']
while 1 :
    res = ''
    a = input()
    if a == ".\n" :
        break
    for i in a :
        if i in text:
            res += i
    while 1 :
        res = res.replace("[]", '').replace("()", '')
        if res == res.replace("[]", '').replace("()", ''):
            break
    if res == '' :
        print('yes')
    else :
        print('no')