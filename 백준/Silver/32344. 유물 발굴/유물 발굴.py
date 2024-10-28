import sys
t = sys.stdin.readline
R, C = map(int, t().split())
N = int(t())
list = [[R+1, 0, C+1, 0] for _ in range(N+1)]
for _ in range(N) :
    a, b, c = map(int, t().split())
    list[a] = [min(list[a][0], b), max(list[a][1], b), min(list[a][2], c), max(list[a][3], c)]

mn, flag = -1, 0
for n, (a,b,c,d) in enumerate(list[::-1]) :
    if a <= b and c <= d and mn <= (b-a+1) * (d-c+1) :
        mn = (b-a+1) * (d-c+1)
        flag = N-n

print(flag, mn)