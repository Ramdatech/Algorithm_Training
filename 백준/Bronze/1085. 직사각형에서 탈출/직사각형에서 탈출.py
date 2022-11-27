import sys
input = sys.stdin.readline
res = []
x, y, w, h = map(int,input().strip().split())
list = [x, y, w-x, h-y]
print(min(list))