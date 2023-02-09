import sys
t = sys.stdin.readline
k,d,a = map(int,t().split('/'))
if k+a < d or d==0 :
    print('hasu')
else :
    print('gosu')