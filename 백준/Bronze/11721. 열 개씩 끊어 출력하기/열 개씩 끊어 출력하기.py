import sys
input = sys.stdin.readline
n = input()
for i in range(len(n)//10+1):
    print(n[i*10:(i+1)*10])