import sys
input = sys.stdin.readline
a,b,c = map(int, input().split())
d = a * 3600 + b * 60 + c + int(input())
print(d//3600%24, (d%3600)//60, (d%3600)%60)