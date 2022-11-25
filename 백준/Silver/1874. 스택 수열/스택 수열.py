import sys
input = sys.stdin.readline
n = int(input())
li, li2 = [0], [0]
res = []
max = 0
for i in range(n) :
    a = int(input().strip())
    if max < a :
        for i in range(max, a):
            li.append(i + 1)
            res.append("+")
        max = a
    if a == li[-1] :
        li2.append(li.pop(-1))
        res.append("-")

if li[-1] == 0 :
    print('\n'.join(res))
else :
    print("NO")