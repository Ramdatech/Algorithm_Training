import sys
sys.setrecursionlimit(5000)
t = sys.stdin.readline
n, m = map(int, t().split())
ls = [list(map(int, t().split())) for _ in range(n)]
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dp = [[0] * m for _ in range(n)]
vst = [[False] * m for _ in range(n)]

def dfs(x, y):
    if [x, y] == [n-1, m-1]:
        return 1
    if vst[x][y]:
        return dp[x][y]
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0 <=nx<n and 0<=ny<m and ls[nx][ny] < ls[x][y] :
            dp[x][y] += dfs(nx, ny)
    vst[x][y] = True
    return dp[x][y]

print(dfs(0, 0))