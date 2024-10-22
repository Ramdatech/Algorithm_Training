import sys
from collections import deque
t = sys.stdin.readline
chd = {}
for _ in range(12):
    a, b = map(int, t().split())
    if a not in chd:
        chd[a] = []
    if b not in chd:
        chd[b] = []
    chd[a].append(b)
    chd[b].append(a)

def find_loop(stt):
    que = deque([[stt, []]])
    while que:
        cur, path = que.popleft()
        if cur == stt and len(path) == 5 and path[1] != path[3]:
            return path
        if len(path) == 6:
            continue
        for nxt in chd[cur]:
            if not path or nxt != path[-1]:
                que.append([nxt, path + [cur]])
    return []

def bfs(stt) :
    que = deque([stt])
    vst = [False] * 13
    vst[stt] = True
    while que :
        cur = que.popleft()
        for nxt in chd[cur] :
            if not vst[nxt] and nxt not in ans:
                vst[nxt] = True
                que.append(nxt)
    return sum(vst)

ans = []
for i in range(1, 13):
    ans = find_loop(i)
    if ans:
        break
dicts = {bfs(p):p for p in ans}
r_dicts = {p:bfs(p) for p in ans}
for i in chd[dicts[1]]:
    if r_dicts[i] == 2 :
        print(i)