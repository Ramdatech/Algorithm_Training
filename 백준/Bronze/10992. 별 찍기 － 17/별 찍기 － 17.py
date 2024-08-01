t = int(input())
for i in range(1, t):
    print(end=(t-i)*" ")
    print(end="*")
    if 2*i-3 > 0 :
        print(end=(2*i-3)*" ")
        print(end="*")
    print()
else :
    print((2*t-1)*"*")