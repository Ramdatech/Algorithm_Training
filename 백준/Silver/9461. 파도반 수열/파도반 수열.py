mem = {0 : 0,
       1 : 1,
       2 : 1,
       3 : 1,
       4 : 2,
       5 : 2,
       6 : 3,
       7 : 4,
       8 : 5,
       9 : 7,
       10 : 9}
def dp(num):
    if num in mem.keys():
        return mem[num]
    else :
        mem[num] = dp(num-5) + dp(num-1)
        return mem[num]

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
for i in range(n) :
    print(dp(int(input())))