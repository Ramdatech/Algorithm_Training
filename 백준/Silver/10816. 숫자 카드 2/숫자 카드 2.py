import sys
from collections import Counter
input = sys.stdin.readline
n = int(input().strip())
ls = Counter(list(map(int,input().strip().split())))
m = int(input().strip())
for i in list(map(int,input().strip().split())):
    print(ls.get(i,0), end=' ')