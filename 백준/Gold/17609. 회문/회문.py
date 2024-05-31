import sys
from collections import deque
t = sys.stdin.readline
n = int(t())
for _ in range(n):
    s = t().strip()
    que = deque([(0, len(s)-1, 0)])
    res = 2
    while que :
        stt, end, flag = que.popleft()
        if stt > end :
            res = min(res, flag)
            continue
        if flag == 2 : continue

        if s[stt] == s[end]:
            que.append((stt+1, end-1, flag))
        if s[stt] != s[end] and s[stt+1] == s[end]:
            que.append((stt+1, end, flag+1))
        if s[stt] != s[end] and s[stt] == s[end-1]:
            que.append((stt, end-1, flag+1))
    print(res)