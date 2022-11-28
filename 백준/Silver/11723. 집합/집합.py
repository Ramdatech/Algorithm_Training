import sys
input = sys.stdin.readline
allset = [str(x) for x in range(1, 21)]
n = int(input())
res = set()
for i in range(n):
    command = input().strip().split(" ")
    if command[0] == 'add' :
        res |= {command[1]}
    elif command[0] == 'remove' :
        res -= {command[1]}
    elif command[0] == 'check' :
        print(len(res&{command[1]}))
    elif command[0] == 'toggle' :
        res ^= {command[1]}
    elif command[0] == 'all' :
        res = set(allset[:])
    elif command[0] == 'empty' :
        res = set()