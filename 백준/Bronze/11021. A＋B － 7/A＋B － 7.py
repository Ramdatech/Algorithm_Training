import sys
a = int(sys.stdin.readline())
arr = []
for i in range(a):
    arr.append(sum(list(map(int,sys.stdin.readline().split()))))

for num, i in enumerate(arr):
    print("Case #{}: {}".format(num+1, i))