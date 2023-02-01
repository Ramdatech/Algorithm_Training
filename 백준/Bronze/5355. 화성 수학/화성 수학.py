import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    ls = input().split()
    num = float(ls.pop(0))
    for i in ls :
        if i == "@":
            num *= 3
        elif i =="%" :
            num += 5
        elif i == '#':
            num -= 7
    print('{:.2f}'.format(num))