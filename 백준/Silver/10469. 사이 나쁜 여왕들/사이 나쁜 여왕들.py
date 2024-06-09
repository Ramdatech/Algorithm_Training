import sys
t = sys.stdin.readline
queens = []
for i in range(8) :
    tmp = t().strip()
    if "*" in tmp :
        queens.append((i, tmp.index("*")))

if len(queens) != 8 :
    print("invalid")
    exit()
    
for x, y in queens :
    for i in range(1, 8) :
        if (x, (y+i)%8) in queens or ((x+i)%8, y) in queens :
            print("invalid")
            exit()
    for pos in [(x+dx, y+dy) for dx in range(-8, 8) for dy in range(-8, 8) if 0<=x+dx<8 and 0<=y+dy<8 and (x,y) != (x+dx, y+dy) and abs(dx) == abs(dy)] :
        if pos in queens :
            print("invalid")
            exit()
print("valid")