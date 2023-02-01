import sys
from itertools import combinations
for input in sys.stdin :
    a = list(map(int, input.split()))
    if a == [0] :
        break
    b = list(combinations(a[1:], 6))
    for i in b :
        print(*sorted(list(i)))
    else :
        print("")