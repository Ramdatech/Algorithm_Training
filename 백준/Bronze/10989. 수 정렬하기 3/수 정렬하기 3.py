import sys
t = sys.stdin.readline
n = int(t())
li = [0] * 10001
for _ in range(n):
    a = int(t())
    li[a] += 1

for idx, i in enumerate(li) : 
    if i : 
        for _ in range(i):
            print(idx)