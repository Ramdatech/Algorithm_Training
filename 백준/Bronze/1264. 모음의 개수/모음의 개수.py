import sys
input = sys.stdin.readline
ls = ['a', 'e', 'i', 'o', 'u']
while 1:
    t = input().strip()
    if t == "#" :
        break
    t = [x for x in list(t.lower()) if x in ls]
    print(len(t))