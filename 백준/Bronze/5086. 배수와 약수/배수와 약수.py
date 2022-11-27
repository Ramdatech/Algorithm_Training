import sys
input = sys.stdin.readline
while 1 :
    n, m = map(int, input().strip().split())
    if n == 0 and m == 0 :
        break
    elif n == 0 or m == 0 :
        print('neither')
        break
    elif n%m == 0 :
        print('multiple')
    elif m%n == 0 :
        print('factor')
    else :
        print('neither')