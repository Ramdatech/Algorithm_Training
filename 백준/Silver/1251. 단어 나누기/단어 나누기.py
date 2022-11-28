import sys
input = sys.stdin.readline
x = str(input().strip())
x = x[::-1]
res = []
for i in range(1, len(x)):
    for j in range(i+1, len(x)):
        res.append(x[j:]+x[i:j]+x[:i])
print(sorted(res)[0])