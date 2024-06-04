import sys
t = sys.stdin.readline
n = int(t())
div = int(1e6)
ls = [0, 1]
s = div//10*15
for i in range(2,s):
    ls.append(ls[i-1]+ls[i-2])
    ls[i] %= div
print(ls[n%s])