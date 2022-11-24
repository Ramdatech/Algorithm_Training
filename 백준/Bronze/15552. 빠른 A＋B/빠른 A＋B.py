import sys
a = int(sys.stdin.readline())
arr = []
for i in range(a):
    arr.append(list(map(int,sys.stdin.readline().split())))

for i in arr :
    print(sum(i))