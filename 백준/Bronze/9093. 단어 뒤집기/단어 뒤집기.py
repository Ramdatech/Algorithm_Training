import sys
input = sys.stdin.readline
n = int(input())
for i in range(n) :
    a = input().strip()
    a = a[::-1].split(" ")
    print(" ".join(a[::-1]))