import sys
input = sys.stdin.readline
a, b = map(int, input().strip().split())
dict = {}
for i in range(a) :
    m = sys.stdin.readline().strip()
    dict[m] = i+1
    dict[str(i+1)] = m

for _ in range(b):
    m = sys.stdin.readline().strip()
    print(dict[m])