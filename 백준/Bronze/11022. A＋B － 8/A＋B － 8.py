import sys
a = int(sys.stdin.readline())
arr = []
for i in range(a):
    arr.append(list(map(int,sys.stdin.readline().split())))

for num, i in enumerate(arr):
    print("Case #{}: {} + {} = {}".format(num+1, i[0], i[1], sum(i)))