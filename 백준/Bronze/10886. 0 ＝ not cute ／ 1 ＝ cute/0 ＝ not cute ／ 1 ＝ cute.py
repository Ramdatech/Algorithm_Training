import sys
input = sys.stdin.readline
n = int(input())
res = 0
for i in range(n) :
    res += int(input())
if res > n/2 :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")
    