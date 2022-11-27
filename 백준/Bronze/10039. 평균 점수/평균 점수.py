import sys
input = sys.stdin.readline
res = 0
for i in range(5) :
    n = int(input())
    if n <= 40 :
        n = 40
    res += n
print(int(res/5))