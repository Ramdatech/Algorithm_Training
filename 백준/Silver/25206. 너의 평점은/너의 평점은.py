div = 0
total = 0
for i in range(20):
    a, b, c = input().split()
    if c == "P" :
        pass
    elif c == "F" : 
        div += int(b[0])
        total += 0
    else :
        var = 0.5 if c[1] == "+" else 0
        div += int(b[0])
        total += (69-ord(c[0]) + var) * int(b[0])
print(total/div)