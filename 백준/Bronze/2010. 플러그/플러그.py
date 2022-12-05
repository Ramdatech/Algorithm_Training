import sys
input = sys.stdin.readline
n = int(input())
result = 0
for _ in range(n) :
    result += int(input()) - 1
print(result+1)