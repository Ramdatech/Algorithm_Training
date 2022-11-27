import sys
input = sys.stdin.readline
while 1 :
    li = list(map(int,input().strip().split()))
    if sum(li) == 0 :
        break
    a = max(li) **2
    li.remove(max(li))
    b = li[0] ** 2
    c = li[1] ** 2
    if a == b+c :
        print('right')
    else :
        print('wrong')