n = int(input())
s = set()
for _ in range(n) :
    a, b = input().split()
    if b == "enter" :
        s.add(a)
    else :
        s.remove(a)

print(*sorted(list(s), reverse=True), sep="\n")