import sys
t = list(map(int, sys.stdin.readline().split()))
res = 0 
for i in t : 
    res += i**2
print(res%10)