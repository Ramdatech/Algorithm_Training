import sys
t = sys.stdin.readline

n, idx = int(t()), 0
arr = [[] for _ in range(n)]
def chk(lst):
    for l in lst :
        if len(set(l)) != 9: return False
    return True

for c in range(n*10-1) :
    if (tmp := t().strip()) != "":
        arr[idx].append(list(map(int, tmp.split())))
    else:
        idx += 1

for i, lst in enumerate(arr):
    q = f"Case {i+1}:"
    if chk(lst):
        if chk(list(zip(*lst))):
            if chk([sum([lst[i+m][j:j+3] for m in range(3)], []) for i in [0, 3, 6] for j in [0, 3, 6]]):
                print(q, "CORRECT")
                continue
    print(q, "INCORRECT")