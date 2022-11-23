import sys
input = sys.stdin.readline
a = int(input().strip())
b = input().strip()
for i in b[::-1] :
    print(int(i) * a)
print(a*int(b))