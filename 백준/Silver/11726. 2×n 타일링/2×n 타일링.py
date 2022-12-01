mem = {0 : 0,
       1 : 1,
       2 : 2}
def dp(num):
    if num in mem.keys() :
        return mem[num]
    else :
        mem[num] = dp(num-1) + dp(num-2)
        return mem[num]

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
print(dp(int(input()))%10007)