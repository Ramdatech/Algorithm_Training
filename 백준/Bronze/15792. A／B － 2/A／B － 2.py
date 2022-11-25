import sys
input = sys.stdin.readline
n, m = map(float, input().split())
count = 0
res = f'{int(n//m)}.'
while 1 :
    n = (n%m)*10
    res += str(int(n//m))
    count += 1
    if count == 1000 :
        break
print(res)