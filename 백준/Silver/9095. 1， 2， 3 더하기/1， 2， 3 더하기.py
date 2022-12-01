def dp(num):
    arr = [0, 1, 2, 4]
    if num <= 0 :
        return 0
    elif num < 4:
        return arr[num]
    return dp(num-1) + dp(num-2) + dp(num-3)

import sys
input = sys.stdin.readline
n = int(input())
for _ in range(n):
    print(dp(int(input())))
    
