import sys
t = int(sys.stdin.readline())
res = 0
count = 0
while t >= 0:
    count += 1
    t -= count
print(count-1)