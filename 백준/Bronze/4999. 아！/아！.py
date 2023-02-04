import sys
t = sys.stdin.readline
x = [len(t()) for x in range(2)]
if x[0]>=x[1]:
    print('go')
else :
    print('no')