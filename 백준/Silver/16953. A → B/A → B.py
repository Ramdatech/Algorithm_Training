from collections import deque
n, m = map(int, input().split())

def bfs(stt) :
    que = deque([(stt, 1)])
    vst = set()
    while que :
        x, cnt = que.popleft()
        if x in vst or x > m: continue
        vst.add(x)
        if x == m :
            return cnt

        que.append((x*2, cnt+1))
        que.append((x*10+1, cnt+1))
    return -1

print(bfs(n))
