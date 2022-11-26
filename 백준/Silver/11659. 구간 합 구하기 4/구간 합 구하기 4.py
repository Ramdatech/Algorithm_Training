import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers_sum = []
for idx, x in enumerate(numbers):
    if idx == 0:
        numbers_sum.append(x)
        continue
    else:
        numbers_sum.append(numbers_sum[-1] + x)

for i in range(m):
    x, y = map(int, input().split())
    if x - 2 == -1 :
        print(numbers_sum[y - 1])
    else :
        print(numbers_sum[y - 1] - numbers_sum[x - 2])