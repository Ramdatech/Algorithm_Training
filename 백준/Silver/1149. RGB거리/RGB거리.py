import sys
t = sys.stdin.readline
n = int(t())
ls = [list(map(int, t().split())) for _ in range(n)]
mp = [[0]*3 for _ in range(n)]

mp[0] = [x for x in ls[0]]
for i in range(1, n) :
    mp[i][0] = ls[i][0] + min(mp[i-1][1], mp[i-1][2])
    mp[i][1] = ls[i][1] + min(mp[i-1][0], mp[i-1][2])
    mp[i][2] = ls[i][2] + min(mp[i-1][0], mp[i-1][1])

print(min(mp[n-1]))