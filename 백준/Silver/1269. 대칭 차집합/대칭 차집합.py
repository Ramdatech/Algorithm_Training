import sys
input = sys.stdin.readline
n, m = map(int, input().split())
A = set(input().strip().split())
B = set(input().strip().split())
print(len((A-B)|(B-A)))