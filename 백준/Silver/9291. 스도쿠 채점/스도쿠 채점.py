import sys
t = sys.stdin.readline

def chk(lst):
    for l in lst :
        if len(set(l)) != 9:
            return False
    return True

n = int(t())
idx = 0
arr = [[] for _ in range(n)]
for c in range(n*10-1) :
    tmp = t().strip()
    if tmp != "":
        arr[idx].append(list(map(int, tmp.split())))
    else:
        idx += 1

for i, lst in enumerate(arr):
    q = f"Case {i+1}:"
    if chk(lst):
        if chk(list(zip(*lst))):
            if chk([lst[i][j:j+3] + lst[i+1][j:j+3] + lst[i+2][j:j+3] for i in range(0, 9, 3) for j in range(0, 9, 3)]):
                print(q, "CORRECT")
                continue
    print(q, "INCORRECT")
