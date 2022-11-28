import sys
input = sys.stdin.readline
n = int(input().strip())
res = set()
for i in range(10000) :
    temp = f'000{i}'
    for j in range(len(temp)+1) :
        a = int(temp[0:j] + "666" + temp[j:])
        res.add(a)
res = sorted(list(res))
print(res[n-1])