mem = {0 : [0, [1, 0]],
       1 : [1, [0, 1]]}
def dp(num):
    if num in mem.keys():
        return mem[num]
    else :
        dp1  = dp(num-1)
        dp2  = dp(num-2)
        mem[num] = [dp1[0]+dp2[0], [a+b for a, b in zip(dp1[1], dp2[1])]]
        return mem[num]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
for i in range(n) :
    print(*dp(int(input()))[1])