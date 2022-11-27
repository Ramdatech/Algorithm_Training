import sys
t = sys.stdin.readline().strip()
res = 0
if t[0] != "F" :
    res = 4-(ord(t[0])-ord("A"))
    if t[1] == "-" : res -= 0.3
    elif t[1] == "+" : res += 0.3
print(f"{res:.1f}")