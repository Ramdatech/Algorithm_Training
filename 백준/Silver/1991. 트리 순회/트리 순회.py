n = int(input())
d = {}
for _ in range(n):
    a, *b = input().split()
    d[a] = b
z = [""]*3
def Z(c) :
    z[0]+=c
    o, p = [x!="." for x in d[c]]
    if o : Z(d[c][0])
    z[1]+=c
    if p : Z(d[c][1])
    z[2]+=c
Z("A")
print(*z, sep="\n")