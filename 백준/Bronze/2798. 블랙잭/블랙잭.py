import sys
input = sys.stdin.readline
n, m = map(int, input().split())
li = list(map(int, input().split()))
sub = [300000, 0]
for x in range(n-2) :
    for y in range(x+1, n-1) :
        for z in range(y+1, n) :
            sum = li[x] + li[y] + li[z]
            if m-sum < sub[0] and m-sum >= 0 :
                sub = [m-sum, sum]
print(sub[1])