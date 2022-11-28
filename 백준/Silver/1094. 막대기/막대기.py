import sys
input = sys.stdin.readline
x = int(input())
bar = [64]

while 1:
    if x == 0 :
        bar = 0
        break
    elif sum(bar) > x :
        bar = bar[:-1] + [bar[-1]*0.5]*2
        if sum(bar[:-1]) >= x :
            bar = bar[:-1]
    else :
        bar = len(bar)
        break
print(bar)