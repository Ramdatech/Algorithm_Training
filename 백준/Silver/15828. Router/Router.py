import sys
input = sys.stdin.readline
n = int(input().strip())
buff = []
while 1:
    a = int(input().strip())
    if a > 0:
        if len(buff) == n :
            pass
        else :
            buff.append(str(a))
    elif a == 0 and len(buff) > 0:
        buff.pop(0)
    elif a == -1 :
        break

if buff :
    print(" ".join(buff))
else :
    print('empty')