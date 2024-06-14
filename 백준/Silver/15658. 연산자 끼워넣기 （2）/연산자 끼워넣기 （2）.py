import sys
t = sys.stdin.readline
n = int(t())
ls = list(map(int,t().split()))
cmd = list(map(int,t().split()))

mx, mn = -1e12, 1e12
def recur(cur, var, cm):
    global mx, mn
    if cur == n-1:
        mx = max(mx, var)
        mn = min(mn, var)
        return

    if cm[0] > 0:
        recur(cur+1, var+ls[cur+1], [cm[0]-1, cm[1], cm[2], cm[3]])
    if cm[1] > 0:
        recur(cur+1, var-ls[cur+1], [cm[0], cm[1]-1, cm[2], cm[3]])
    if cm[2] > 0:
        recur(cur+1, var*ls[cur+1], [cm[0], cm[1], cm[2]-1, cm[3]])
    if cm[3] > 0:
        recur(cur+1, int(var/ls[cur+1]), [cm[0], cm[1], cm[2], cm[3]-1])

recur(0, ls[0], cmd)
print(mx)
print(mn)