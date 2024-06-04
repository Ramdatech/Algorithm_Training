import sys
from collections import deque
t = sys.stdin.readline
R, C = map(int, t().split())
ls = [t().strip() for _ in range(R)]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
que_j = deque()
que_f = deque()

for r in range(R):
    for c in range(C):
        if ls[r][c] == 'J':
            que_j.append((r, c, 0))  # 지훈이 위치 (x, y, 시간)
        elif ls[r][c] == 'F':
            que_f.append((r, c, 0))  # 불 위치 (x, y, 시간)

while que_j:
    for _ in range(len(que_f)):
        x, y, _ = que_f.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and ls[nx][ny] == '.':
                ls[nx] = ls[nx][:ny] + 'F' + ls[nx][ny + 1:]
                que_f.append((nx, ny, 0))

    for _ in range(len(que_j)):
        x, y, time = que_j.popleft()
        if x == 0 or x == R - 1 or y == 0 or y == C - 1:  # 가장자리에 도달하면
            print(time + 1)
            sys.exit()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and ls[nx][ny] == '.':
                ls[nx] = ls[nx][:ny] + 'J' + ls[nx][ny + 1:]
                que_j.append((nx, ny, time + 1))

print("IMPOSSIBLE")