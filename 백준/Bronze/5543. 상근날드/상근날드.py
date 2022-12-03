import sys
input = sys.stdin.readline
burger = sorted([int(input()) for _ in range(3)])
drink = sorted([int(input()) for _ in range(2)])
print(burger[0]+drink[0]-50)