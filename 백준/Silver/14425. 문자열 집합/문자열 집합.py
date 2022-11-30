import sys
input = sys.stdin.readline
a, b = map(int, input().strip().split())
res = set()
score = 0
for i in range(a) :
    m = sys.stdin.readline().strip()
    res.add(m)
for _ in range(b):
    m = sys.stdin.readline().strip()
    if m in res :
        score += 1

print(score)