import sys
input = sys.stdin.readline
n = int(input().strip())
ent = [0,0]
direct = [0,0]
size = []

for _ in range(6) :
    x, y = map(int, input().strip().split())
    if x <= 2 and ent[0] <= y:
        ent[0] = y
        direct[0] = x
    elif x > 2 and ent[1] <= y :
        ent[1] = y
        direct[1] = x

    size.append(y)
size = size*2
for i in range(len(size)) :
    if size[i:i+2] == ent or size[i:i+2] == ent[::-1] :
        area = (ent[0]*ent[1]) - (size[i+3]*size[i+4])
        print(area * n)
        break
