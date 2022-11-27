import sys
a = sys.stdin.readline().strip()
b1 = ord("A")-ord('a')
for i in a:
    if ord(i) < ord('Z') :
        print(chr(ord(i)-b1), end='')
    else :
        print(chr(ord(i)+b1), end='')