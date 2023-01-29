import sys
from itertools import zip_longest

input = sys.stdin.readline
ls = map(int,input().split())
print(sum(ls))