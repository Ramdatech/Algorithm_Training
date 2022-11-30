import sys 
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
li = sorted(li)
res = 0 
for i in range(n) :
    res += sum(li[0:i+1])
print(res)