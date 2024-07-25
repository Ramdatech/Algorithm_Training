n = input()
if 'x' not in n :
    print(0)
elif n[0] == "0" :
    print(0)
elif n[0] == "x" :
    print(1)
elif n[:2] == "-x" :
    print(-1)
else :
    print(n[:n.find("x")])