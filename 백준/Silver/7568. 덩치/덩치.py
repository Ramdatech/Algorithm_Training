import sys
input = sys.stdin.readline
n = int(input().strip())
res = []

for _ in range(n):
    li = list(map(int, input().strip().split()))
    res.append(li)

for i in res:
    count = 1
    for j in res:
        if i[0] < j[0] and i[1] < j[1]:
            count += 1
    print(count, end=' ')