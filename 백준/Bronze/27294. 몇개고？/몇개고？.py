import sys
input = sys.stdin.readline
a, b = map(int,input().split())
if (a<12 or a>16) or b==1 :
    print(280)
else :
    print(320)