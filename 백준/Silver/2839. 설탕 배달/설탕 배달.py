import sys
t = sys.stdin.readline
a = int(t())
score = -1
for i in range(0, 5):
    x = (4-i) * 3
    if a>=x :
        y = a-x
        if y%5 == 0 :
            score = y//5 + (4-i)
            break

print(score)