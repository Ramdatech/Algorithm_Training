import sys
t = sys.stdin.readline
ls = [0]*26
for i in t().strip():
    ls[ord(i)-97] += 1
print(*ls)