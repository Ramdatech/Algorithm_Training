import sys
a = list(sys.stdin.readline().strip())
a.sort(reverse=True)
for i in a :
    print(i, end="")