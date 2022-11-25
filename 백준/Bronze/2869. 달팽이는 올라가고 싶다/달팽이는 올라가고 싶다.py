import sys
import math
t = sys.stdin.readline
a, b, v = map(int, t().split())

res = 1
if v > a :
    v = v-a
    res += math.ceil(v/(a-b))

print(res)