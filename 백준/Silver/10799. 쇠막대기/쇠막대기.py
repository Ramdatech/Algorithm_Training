import sys
b = sys.stdin.readline().strip().replace("()", "@")
inhole = 0
cutwood = 0
for i in b:
    if i == "(" :
        inhole += 1
    elif i == ")" :
        inhole -= 1
        cutwood += 1
    elif i == "@" :
        cutwood += inhole
print(cutwood)