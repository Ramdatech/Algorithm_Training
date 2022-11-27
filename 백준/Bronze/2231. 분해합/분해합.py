import sys
input = sys.stdin.readline
n = int(input())
m = n - len(str(n)) * 9
if m < 0 :
    m = 0
res = 0
for i in range(m, n+1):
    if n == i + sum(list(map(int, str(i)))) :
        res = i
        break
print(res)