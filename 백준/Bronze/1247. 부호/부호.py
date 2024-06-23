import sys
t = sys.stdin.readline

for _ in range(3):
    n = int(t())
    res = 0
    for _ in range(n) :
        res += int(t())
    match res :
        case 0 : print("0")
        case _ : print("+" if res > 0 else "-")