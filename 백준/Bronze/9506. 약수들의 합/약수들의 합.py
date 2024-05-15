import sys
from collections import deque
t = sys.stdin.readline

while 1 :
    m = int(t().strip())
    if m == -1 :
        break
    vst = set()
    for i in range(1, int((m**0.5))+1) :
        if m%i == 0 :
            vst.add(i)
            vst.add(m//i)
    vst = sorted(list(vst))
    if sum(vst[:-1]) == m :
        print(f"{m} = {' + '.join(map(str, vst[:-1]))}")
    else :
        print(f"{m} is NOT perfect.")