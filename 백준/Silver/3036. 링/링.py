import sys
import math
input = sys.stdin.readline
n = int(input())
li1 = list(map(int, input().strip().split()))
first = li1.pop(0)
for i in li1:
    a = math.gcd(first, i)
    print(f"{first//a}/{i//a}")