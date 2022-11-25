import sys
a = sys.stdin.readline().strip()
li = []
print(*[a.find(chr(x)) for x in range(ord('a'), ord('z')+1)])
