import sys
input = sys.stdin.readline
n = int(input())
li1 = list(map(int, input().strip().split()))
m = int(input())
li2 = list(map(int, input().strip().split()))
li3 = set(li1) & set(li2)
for i in list(li2) :
    if i in li3:
        print(1, end=' ')
    else :
        print(0, end=' ')